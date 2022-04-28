"""empty message

Revision ID: 429fc9d04a4f
Revises: b1a584f71418
Create Date: 2022-04-27 05:28:48.429891

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '429fc9d04a4f'
down_revision = 'b1a584f71418'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('properties', 'title',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    op.alter_column('properties', 'description',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('properties', 'rooms',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('properties', 'baths',
               existing_type=sa.REAL(),
               nullable=True)
    op.alter_column('properties', 'price',
               existing_type=sa.REAL(),
               nullable=True)
    op.alter_column('properties', 'type',
               existing_type=sa.VARCHAR(length=10),
               nullable=True)
    op.alter_column('properties', 'location',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    op.alter_column('properties', 'photo',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('properties', 'photo',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
    op.alter_column('properties', 'location',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
    op.alter_column('properties', 'type',
               existing_type=sa.VARCHAR(length=10),
               nullable=False)
    op.alter_column('properties', 'price',
               existing_type=sa.REAL(),
               nullable=False)
    op.alter_column('properties', 'baths',
               existing_type=sa.REAL(),
               nullable=False)
    op.alter_column('properties', 'rooms',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('properties', 'description',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('properties', 'title',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
    # ### end Alembic commands ###
