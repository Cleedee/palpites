"""criar tabela torneio

Revision ID: 6e3d9e28269d
Revises: a344b1ce4a7d
Create Date: 2022-03-29 11:22:23.747152

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6e3d9e28269d'
down_revision = 'a344b1ce4a7d'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'torneio',
        sa.Column('id', sa.Integer, primary_key = True),
        sa.Column('nome', sa.String(60)),
        sa.Column('responsavel_id', sa.Integer)
    )


def downgrade():
    op.drop_table('torneio')
