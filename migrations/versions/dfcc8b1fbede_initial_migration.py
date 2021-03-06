"""Initial Migration

Revision ID: dfcc8b1fbede
Revises: 71d12b45c4d2
Create Date: 2021-08-15 11:21:56.864951

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dfcc8b1fbede'
down_revision = '71d12b45c4d2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reviews',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('movie_id', sa.Integer(), nullable=True),
    sa.Column('movie_title', sa.String(), nullable=True),
    sa.Column('image_path', sa.String(), nullable=True),
    sa.Column('movie_review', sa.String(), nullable=True),
    sa.Column('posted', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('users', sa.Column('reviews', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'users', 'users', ['reviews'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.drop_column('users', 'reviews')
    op.drop_table('reviews')
    # ### end Alembic commands ###
