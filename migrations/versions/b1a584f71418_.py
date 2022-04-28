"""empty message

Revision ID: b1a584f71418
Revises: 09fec18014ba
Create Date: 2022-04-27 05:17:36.983499

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b1a584f71418'
down_revision = '09fec18014ba'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('properties', sa.Column('id', sa.Integer(), nullable=False))
    op.drop_column('properties', 'propertyid')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('properties', sa.Column('propertyid', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_column('properties', 'id')
    # ### end Alembic commands ###
