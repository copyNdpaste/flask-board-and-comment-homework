"""create_keywords_table

Revision ID: 808165e9ffaa
Revises: f216acafbcc2
Create Date: 2022-07-18 16:36:14.161892

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "808165e9ffaa"
down_revision = "f216acafbcc2"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "keywords",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("keyword", sa.String(length=50), nullable=False),
        sa.Column("writer", sa.String(length=30), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade():
    op.drop_table("keywords")
