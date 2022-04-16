"""campo do torneio na tabela rodada

Revision ID: 4c7ceaadf2cf
Revises: 5e3a13f91932
Create Date: 2022-03-29 13:29:49.012448

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4c7ceaadf2cf'
down_revision = '5e3a13f91932'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('rodada', sa.Column('torneio_id', sa.Integer))


def downgrade():
    op.drop_column('rodada', 'torneio_id')
