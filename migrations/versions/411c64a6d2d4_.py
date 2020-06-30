"""empty message

Revision ID: 411c64a6d2d4
Revises: f17a3b62d8be
Create Date: 2019-11-28 22:27:50.812545

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '411c64a6d2d4'
down_revision = 'f17a3b62d8be'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('cms_user', '_password')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cms_user', sa.Column('_password', mysql.VARCHAR(length=50), nullable=False))
    # ### end Alembic commands ###