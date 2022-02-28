"""criar tabela grupo

Revision ID: a39538758585
Revises: dd8917fb45b8
Create Date: 2022-02-28 07:58:02.325651

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a39538758585'
down_revision = 'dd8917fb45b8'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'grupo',
        sa.Column('id', sa.Integer, primary_key = True),
        sa.Column('nome', sa.String(60)),
        sa.Column('dono', sa.Integer),
        sa.Column('ativo', sa.Boolean)
    )


def downgrade():
    op.drop_table('grupo')
