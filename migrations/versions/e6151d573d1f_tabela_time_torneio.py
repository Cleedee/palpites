"""tabela time_torneio

Revision ID: e6151d573d1f
Revises: 4c7ceaadf2cf
Create Date: 2022-03-30 13:41:08.290758

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e6151d573d1f'
down_revision = '4c7ceaadf2cf'
branch_labels = None
depends_on = None


def upgrade():
        op.create_table(
            'time_torneio',
            sa.Column('time_id', sa.Integer, primary_key = True),
            sa.Column('torneio_id', sa.Integer, primary_key = True),
        )


def downgrade():
    op.drop_table('time_torneio')
