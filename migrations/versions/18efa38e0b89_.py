"""empty message

Revision ID: 18efa38e0b89
Revises: 390c0c492469
Create Date: 2017-03-24 22:06:00.461952

"""

# revision identifiers, used by Alembic.
revision = '18efa38e0b89'
down_revision = '390c0c492469'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('foot_shape', sa.Integer(), server_default="0"))
    op.add_column('user', sa.Column('split_shoe_info', sa.Integer(), server_default="0"))
    ### end Alembic commands ###

def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user') as batch_op:
        batch_op.drop_column('split_shoe_info')
        batch_op.drop_column('foot_shape')
    ### end Alembic commands ###
