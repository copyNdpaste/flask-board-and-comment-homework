"""create_comments_table

Revision ID: f216acafbcc2
Revises: 017d43180672
Create Date: 2022-07-18 16:36:07.393392

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "f216acafbcc2"
down_revision = "017d43180672"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "comments",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("contents", sa.String(length=1000), nullable=False),
        sa.Column("writer", sa.String(length=30), nullable=False),
        sa.Column("parent_id", sa.Integer(), nullable=True),
        sa.Column("board_id", sa.Integer(), nullable=False),
        sa.Column("created_at", sa.String(length=30), nullable=False),
        sa.ForeignKeyConstraint(
            ["board_id"],
            ["boards.id"],
        ),
        sa.ForeignKeyConstraint(
            ["parent_id"],
            ["comments.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade():
    op.drop_table("comments")
