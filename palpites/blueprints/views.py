from collections import namedtuple

from flask import render_template, request, redirect, url_for
from flask_login import login_required

import palpites.ext.repository as rep
import palpites.ext.forms as forms
from palpites.ext import database

def init_app(app):

    @app.get('/')
    def index():
        return render_template('index.html')

    @app.get('/jogadores')
    @login_required
    def jogadores():
        lista = rep.traga_jogadores()
        return render_template('jogadores.html', jogadores=lista)

    @app.get('/rodadas')
    @login_required
    def mostra_rodadas():
        rodadas = rep.traga_rodadas()
        return render_template('rodadas.html', rodadas = rodadas)

    @app.get('/partidas/<int:rodada_id>')
    @login_required
    def mostra_partidas(rodada_id):
        rodada = rep.traga_rodada(rodada_id)
        partidas = rep.traga_partidas_da_rodada(rodada_id)
        return render_template('partidas.html', rodada=rodada, partidas=partidas)

    @app.get('/nova_partida/<int:rodada_id>')
    @login_required
    def nova_partida(rodada_id):
        form = forms.PartidaForm()
        form.rodada_id.data = rodada_id
        form = forms.carregar_selecoes_partida(form, rep)
        return render_template('partida.html', form=form)

    @app.get('/editar_partida/<int:partida_id>')
    @login_required
    def editar_partida(partida_id):
        partida = rep.traga_partida(partida_id)
        form = forms.PartidaForm()
        forms.carregar_partida(form, partida, rep)
        form = forms.carregar_selecoes_partida(form, rep)
        return render_template('partida.html', form=form)

    @app.post('/salvar_partida')
    @login_required
    def salvar_partida():
        form = forms.PartidaForm()
        form = forms.carregar_selecoes_partida(form, rep)
        if form.validate_on_submit():
            # salvar a partida
            if form.partida_id.data:
                partida = rep.traga_partida(form.partida_id.data)
            else:
                partida = database.Partida()
            forms.atualizar_partida(form, partida)
            rep.salve_partida(partida)
            if request.form.get('submit_continuar'):
                return redirect(url_for('nova_partida',rodada_id=partida.rodada_id))
            else:
                return redirect(url_for('mostra_partidas',rodada_id=partida.rodada_id))
        print(form.errors)
        return redirect(url_for('index'))

    @app.post('/salvar_palpite')
    @login_required
    def salvar_palpite():
        form = forms.PalpiteForm()
        if form.validate_on_submit():
            print("Valido")
            palpite = rep.traga_palpite(form.palpite_id.data)
            forms.atualizar_palpite(form, palpite)
            rep.salve_palpite(palpite)
            if request.form.get('submit_salvar'):
                # salvar e sair
                return redirect(url_for('palpites',partida_id=palpite.partida_id))
            else:
                # salvar e seguir
                palpites = rep.traga_palpites_da_rodada_do_jogador_nao_feitos(
                    palpite.partida.rodada_id, palpite.apostador_id)
                if len(palpites) > 0:
                    proximo_palpite = palpites[0]
                    return redirect(url_for('palpite',palpite_id=proximo_palpite.id))
        print(form.errors)
        return redirect(url_for('palpites',partida_id=palpite.partida_id))

    @app.get('/palpites/<partida_id>')
    @login_required
    def palpites(partida_id):
        partida = rep.traga_partida(partida_id)
        lista = rep.traga_palpites_na_partida(partida_id)
        print(len(lista))
        if len(lista) == 0:
            print('Gerar palpites')
            redirect(url_for('gerar_palpites',partida_id=partida_id))
        return render_template('palpites.html', partida=partida,palpites=lista)

    @app.get('/gerar_palpites/<partida_id>')
    @login_required
    def gerar_palpites(partida_id):
        print('Gerando palpites')
        rep.gerar_palpites(partida_id)
        print('Palpites gerados')
        return redirect(url_for('palpites',partida_id=partida_id))

    @app.get('/palpite/<palpite_id>')
    @login_required
    def palpite(palpite_id):
        p = rep.traga_palpite(palpite_id)
        form = forms.PalpiteForm()
        form.palpite_id.data = palpite_id
        form.resultado.data = p.resultado
        return render_template('palpite.html', form=form, palpite=p)

    @app.get('/consolidar/<rodada_id>')
    @login_required
    def consolidar(rodada_id):
        rep.consolidar_rodada(rodada_id)
        return redirect(url_for('jogadores'))

    @app.get('/parciais/<rodada_id>')
    @login_required
    def parciais(rodada_id):
        rodada = rep.traga_rodada(rodada_id)
        parciais = rep.traga_parcial(rodada_id)
        jogadores = rep.traga_jogadores()
        return render_template('parciais.html', rodada=rodada, parciais=parciais,jogadores=jogadores)

    @app.get('/palpites_jogador/<rodada_id>/<jogador_id>')
    @login_required
    def palpites_jogador(rodada_id, jogador_id):
        rodada = rep.traga_rodada(rodada_id)
        palpites = rep.traga_palpites_da_rodada_do_jogador(rodada_id, jogador_id)
        jogador = rep.traga_jogador(jogador_id)
        return render_template('palpites_jogador.html',
            jogador=jogador, rodada=rodada, palpites=palpites)

    @app.get('/time')
    @app.get('/time/<jogador_id>')
    @login_required
    def palpites_errados_time(jogador_id = None):
        times = rep.traga_times()
        Estatistica = namedtuple('Estatistica',['time','pontos'])
        totais = []
        for time in times:
            total: int = 0
            if jogador_id:
                total = rep.total_palpites_errados_por_time(time.id, jogador_id)
            else:
                total = rep.total_palpites_errados_por_time(time.id)
            totais.append(Estatistica(time, total))
        return render_template('time.html', totais=totais)

    @app.get('/nova_rodada')
    @login_required
    def nova_rodada():
        rodadas = [int(r.nome) for r in rep.traga_rodadas()]
        rodadas.sort()
        nova_rodada: int = 1
        if rodadas:
            nova_rodada = rodadas[-1] + 1
        rep.salve_rodada(database.Rodada(nome=str(nova_rodada)))
        return redirect(url_for('mostra_rodadas'))

    @app.get('/times')
    @login_required
    def mostra_times():
        times = rep.traga_times()
        info = [ (time, rep.total_palpites_errados_por_time(time.id)) for time in times ]
        return render_template('times.html', info=info)
