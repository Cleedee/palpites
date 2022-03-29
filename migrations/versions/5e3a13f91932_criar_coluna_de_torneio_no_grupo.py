"""criar coluna de torneio no grupo

Revision ID: 5e3a13f91932
Revises: 6e3d9e28269d
Create Date: 2022-03-29 11:28:10.145385

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5e3a13f91932'
down_revision = '6e3d9e28269d'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('grupo', sa.Column('torneio_id', sa.Integer))


def downgrade():
    op.drop_column('grupo', 'torneio_id')
