"""add last few columns to posts table

Revision ID: 4bb1cb4f6197
Revises: 838b6bb85b1a
Create Date: 2022-01-05 22:01:13.235334

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4bb1cb4f6197'
down_revision = '838b6bb85b1a'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts',sa.Column(
        'published',sa.Boolean,nullable=False,server_default=sa.text('True')
    ),)
     
    op.add_column('posts',sa.Column(
         'created_at',sa.TIMESTAMP(timezone=True),nullable=False,server_default=sa.text('NOW()')
     ))


def downgrade():
    op.drop_column('posts','published')
    op.drop_column('posts','created_at')
