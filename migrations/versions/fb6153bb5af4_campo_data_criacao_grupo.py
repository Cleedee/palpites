"""campo data criacao grupo

Revision ID: fb6153bb5af4
Revises: a39538758585
Create Date: 2022-02-28 14:36:07.267664

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fb6153bb5af4'
down_revision = 'a39538758585'
branch_labels = None
depends_on = None

def upgrade():
    op.add_column('grupo', sa.Column('data_cadastro', sa.DateTime))


def downgrade():
    op.drop_column('grupo', 'data_cadastro')
