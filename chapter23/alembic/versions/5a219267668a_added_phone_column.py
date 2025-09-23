"""added phone column

Revision ID: 5a219267668a
Revises: 32cd882f5f24
Create Date: 2025-09-23 12:18:07.373382

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5a219267668a'
down_revision: Union[str, Sequence[str], None] = '32cd882f5f24'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("users",sa.Column("phone",sa.Integer()))


def downgrade() -> None:
    op.drop_column("users","phone")
