"""empty message

Revision ID: e4a93a09a927
Revises: 0579df9fdd7c
Create Date: 2023-01-27 02:09:40.783448

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e4a93a09a927'
down_revision = '0579df9fdd7c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('people',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('fav_people',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_name', sa.String(length=120), nullable=True),
    sa.Column('people_name', sa.String(length=120), nullable=True),
    sa.ForeignKeyConstraint(['people_name'], ['people.name'], ),
    sa.ForeignKeyConstraint(['user_name'], ['user.email'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('fav_people')
    op.drop_table('people')
    # ### end Alembic commands ###
