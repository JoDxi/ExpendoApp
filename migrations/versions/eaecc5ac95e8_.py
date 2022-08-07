"""empty message

Revision ID: eaecc5ac95e8
Revises: a6bd5275ce84
Create Date: 2022-08-03 13:08:26.206887

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eaecc5ac95e8'
down_revision = 'a6bd5275ce84'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('expenses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('rent', sa.Integer(), nullable=True),
    sa.Column('bills', sa.Integer(), nullable=True),
    sa.Column('groceries', sa.Integer(), nullable=True),
    sa.Column('transportation', sa.Integer(), nullable=True),
    sa.Column('entertainment', sa.Integer(), nullable=True),
    sa.Column('vacation', sa.Integer(), nullable=True),
    sa.Column('miscellaneous', sa.Integer(), nullable=True),
    sa.Column('date', sa.String(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('expenses')
    # ### end Alembic commands ###