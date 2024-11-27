"""empty message

Revision ID: 11ba83e2dd71
Revises: 5639ad89ee50
Create Date: 2021-11-15 11:15:14.060491

"""
import sqlalchemy_utils
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '11ba83e2dd71'
down_revision = '5639ad89ee50'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'can_use_subdomain')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('can_use_subdomain', sa.BOOLEAN(), server_default=sa.text('false'), autoincrement=False, nullable=False))
    # ### end Alembic commands ###