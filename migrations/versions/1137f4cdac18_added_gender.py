"""added gender

Revision ID: 1137f4cdac18
Revises: a11e2d0d0fd
Create Date: 2018-08-26 18:40:21.616487

"""

# revision identifiers, used by Alembic.
revision = '1137f4cdac18'
down_revision = 'a11e2d0d0fd'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('gender', sa.Integer(),
                                    nullable=False, server_default="0"))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user') as batch_op:
        batch_op.drop_column('gender')
    ### end Alembic commands ###