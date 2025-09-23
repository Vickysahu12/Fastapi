"""email column unique

Revision ID: c4833e06399d
Revises: c3b1ac31320e
Create Date: 2025-09-23 12:40:47.209014

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c4833e06399d'
down_revision: Union[str, Sequence[str], None] = 'c3b1ac31320e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with op.batch_alter_table("users") as batch_op:
        batch_op.create_unique_constraint("uq_users_email",["email"])


def downgrade() -> None:
    with op.batch_alter_table("users") as batch_op:
        batch_op.drop_constraint("uq_users_email", type_='unique')
