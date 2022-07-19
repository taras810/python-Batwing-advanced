"""002_create_author_table

Revision ID: 002_create_author_table
Revises: 001_create_book_table
Create Date: 2022-07-16 15:24:59.919031

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '002_create_author_table'
down_revision = '001_create_book_table'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'author',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(), nullable=False, unique=True),
    )


def downgrade() -> None:
    op.drop_table("author")
