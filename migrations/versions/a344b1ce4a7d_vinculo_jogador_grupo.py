"""vinculo jogador grupo

Revision ID: a344b1ce4a7d
Revises: 3f828ac55a84
Create Date: 2022-03-05 22:24:48.006634

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a344b1ce4a7d'
down_revision = '3f828ac55a84'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('jogador', sa.Column('grupo_id', sa.Integer))


def downgrade():
    op.drop_column('jogador', 'grupo_id')
