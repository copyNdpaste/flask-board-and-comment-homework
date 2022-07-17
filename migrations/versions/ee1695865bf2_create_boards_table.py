"""create boards table

Revision ID: ee1695865bf2
Revises: 
Create Date: 2022-07-17 00:58:44.270267

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "ee1695865bf2"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "boards",
        sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
        sa.Column("title", sa.String(50), nullable=False),
        sa.Column("contents", sa.Text(10000), nullable=False),
        sa.Column("writer", sa.String(30), nullable=False),
        sa.Column("password", sa.String(10), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
    )

    op.create_index("title_idx", "boards", ["title"], unique=False),


def downgrade():
    op.drop_table("boards")
