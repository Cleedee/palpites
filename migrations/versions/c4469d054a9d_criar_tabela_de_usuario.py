"""Criar tabela de usuario

Revision ID: c4469d054a9d
Revises: d1967afe0d42
Create Date: 2021-09-06 22:18:21.178212

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c4469d054a9d'
down_revision = 'd1967afe0d42'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'usuario',
        sa.Column('id', sa.Integer, primary_key = True),
        sa.Column('id_alternativo', sa.Unicode),
        sa.Column('apelido', sa.String(60)),
        sa.Column('nome', sa.String(60)),
        sa.Column('senha', sa.String(60)),
        sa.Column('ativo', sa.Boolean)
    )


def downgrade():
    op.drop_table('usuario')
