"""criar coluna pontos

Revision ID: d1967afe0d42
Revises: 
Create Date: 2021-06-27 23:47:46.687122

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd1967afe0d42'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('jogador', sa.Column('pontos', sa.Integer))


def downgrade():
    op.drop_column('jogador', 'pontos')
