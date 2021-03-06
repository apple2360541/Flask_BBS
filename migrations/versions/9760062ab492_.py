"""empty message

Revision ID: 9760062ab492
Revises: 5ddbb7ed4ee9
Create Date: 2019-12-20 18:56:57.093702

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '9760062ab492'
down_revision = '5ddbb7ed4ee9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cms_role', sa.Column('permissions', sa.Integer(), nullable=True))
    op.drop_column('cms_role', 'persimmions')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cms_role', sa.Column('persimmions', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.drop_column('cms_role', 'permissions')
    # ### end Alembic commands ###
