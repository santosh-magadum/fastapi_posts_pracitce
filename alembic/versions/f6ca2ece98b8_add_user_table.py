"""add user table

Revision ID: f6ca2ece98b8
Revises: c5dc7fe49fc4
Create Date: 2022-01-05 21:30:52.074928

"""
from alembic import op
import sqlalchemy as sa 



# revision identifiers, used by Alembic.
revision = 'f6ca2ece98b8'
down_revision = 'c5dc7fe49fc4'
branch_labels = None
depends_on = None


def upgrade():

    op.create_table('users',
     sa.Column('id',sa.Integer(),primary_key=True,nullable=False),
    sa.Column('email',sa.String(200),nullable=False,unique=True),
    sa.Column('password',sa.String(500),nullable=False),
    sa.Column('created_at',sa.TIMESTAMP(timezone=True),nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')

    )


def downgrade():
    op.drop_table('users')
