"""empty message

Revision ID: 748942fac7d7
Revises: 31433e78f79e
Create Date: 2018-09-15 09:40:19.827476

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '748942fac7d7'
down_revision = '31433e78f79e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('ingredient', sa.Column('name', sa.String(length=64), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('ingredient', 'name')
    # ### end Alembic commands ###
