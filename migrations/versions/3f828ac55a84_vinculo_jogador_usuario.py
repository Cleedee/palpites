"""vinculo jogador usuario

Revision ID: 3f828ac55a84
Revises: fb6153bb5af4
Create Date: 2022-03-05 22:15:12.952811

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3f828ac55a84'
down_revision = 'fb6153bb5af4'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('jogador', sa.Column('usuario_id', sa.Integer))


def downgrade():
    op.drop_column('jogador', 'usuario_id')
