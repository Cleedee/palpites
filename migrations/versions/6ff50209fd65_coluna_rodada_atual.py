"""Coluna rodada atual

Revision ID: 6ff50209fd65
Revises: e6151d573d1f
Create Date: 2023-03-30 19:38:00.881290

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6ff50209fd65'
down_revision = 'e6151d573d1f'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('grupo', sa.Column('rodada_atual_id', sa.Integer))


def downgrade():
    op.drop_column('grupo', 'rodada_atual_id')
