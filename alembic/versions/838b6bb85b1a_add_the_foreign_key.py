"""add the foreign key

Revision ID: 838b6bb85b1a
Revises: f6ca2ece98b8
Create Date: 2022-01-05 21:45:37.564534

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql.expression import false


# revision identifiers, used by Alembic.
revision = '838b6bb85b1a'
down_revision = 'f6ca2ece98b8'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts',sa.Column('owner_id',sa.Integer(),nullable=False))
    op.create_foreign_key('post_users_fk',source_table='posts',referent_table='users',
    local_cols=['owner_id'],remote_cols=['id'],ondelete='CASCADE')


def downgrade():
    op.drop_constraint('post_users_fk',table_name='posts')
    op.drop_column('posts','owner_id')
