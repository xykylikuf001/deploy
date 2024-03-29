"""4_step_order

Revision ID: 578d557928f3
Revises: a581bdb2e490
Create Date: 2024-03-29 23:45:30.980210

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '578d557928f3'
down_revision = 'a581bdb2e490'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('protocol_step', sa.Column('step_order', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('protocol_step', 'step_order')
    # ### end Alembic commands ###
