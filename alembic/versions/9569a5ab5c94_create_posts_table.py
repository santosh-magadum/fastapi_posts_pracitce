"""Create Posts table

Revision ID: 9569a5ab5c94
Revises: 
Create Date: 2022-01-05 11:03:57.365311

"""
from alembic import op
import sqlalchemy as sa

from datetime import date
from sqlalchemy.sql import table, column
from sqlalchemy import String, Integer, Date

# revision identifiers, used by Alembic.
revision = '9569a5ab5c94'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts',sa.Column('id',sa.Integer(),nullable=False,primary_key=True),
    sa.Column('title',sa.String(500),nullable=False))

    



    # Create an ad-hoc table to use for the insert statement.
    # accounts_table = table('account',
    #     column('id', Integer),
    #     column('name', String),
    #     column('create_date', Date)
    # )
    # op.create_table(accounts_table)

def downgrade():
    op.drop_table('posts')
