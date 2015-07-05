"""empty message

Revision ID: 43aac6a8018
Revises: 527e6a16a4
Create Date: 2015-07-04 21:23:22.444106

"""

# revision identifiers, used by Alembic.
revision = '43aac6a8018'
down_revision = '527e6a16a4'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('nickname', sa.String(length=32), nullable=False))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'nickname')
    ### end Alembic commands ###
