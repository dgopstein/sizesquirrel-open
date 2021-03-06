"""size_in_user_items

Revision ID: 385e2996a83a
Revises: 4c6234f36920
Create Date: 2016-05-21 16:00:03.958836

"""

# revision identifiers, used by Alembic.
revision = '385e2996a83a'
down_revision = '4c6234f36920'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_item', sa.Column('size_in', sa.String(length=64), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_item') as batch_op:
        batch_op.drop_column('size_in')
    ### end Alembic commands ###
