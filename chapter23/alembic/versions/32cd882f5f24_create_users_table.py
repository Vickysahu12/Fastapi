"""create users table

Revision ID: 32cd882f5f24
Revises: 
Create Date: 2025-09-23 11:54:04.586950

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '32cd882f5f24'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
    "users",
    sa.Column("id", sa.INTEGER, primary_key=True),
    sa.Column("name", sa.String(50), nullable=False),
    sa.Column("email", sa.String, nullable=False),
)


def downgrade() -> None:
    """Downgrade schema."""
    pass
