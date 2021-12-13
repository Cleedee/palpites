"""Campo de papeis

Revision ID: dd8917fb45b8
Revises: c4469d054a9d
Create Date: 2021-09-14 13:01:54.859965

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dd8917fb45b8'
down_revision = 'c4469d054a9d'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('usuario', sa.Column('papeis', sa.String(10)))


def downgrade():
    op.drop_column('usuario', 'papeis')
