"""003_create_book_author_table

Revision ID: 003_create_book_author_table
Revises: 002_create_author_table
Create Date: 2022-07-19 11:16:39.089741

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '003_create_book_author_table'
down_revision = '002_create_author_table'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "book_author",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("book_id", sa.Integer, sa.ForeignKey("book.id")),
        sa.Column("author_id", sa.Integer, sa.ForeignKey("author.id"))
    )


def downgrade() -> None:
    op.drop_table("book_author")
