"""add the content column to posts table

Revision ID: c5dc7fe49fc4
Revises: 9569a5ab5c94
Create Date: 2022-01-05 14:02:41.628314

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c5dc7fe49fc4'
down_revision = '9569a5ab5c94'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts',sa.Column('content',sa.String(500),nullable=False))


def downgrade():
    op.drop_column('posts','content')
    
