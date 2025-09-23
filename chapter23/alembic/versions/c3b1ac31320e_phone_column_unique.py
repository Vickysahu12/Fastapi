"""phone column unique

Revision ID: c3b1ac31320e
Revises: 5a219267668a
Create Date: 2025-09-23 12:30:26.138274

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c3b1ac31320e'
down_revision: Union[str, Sequence[str], None] = '5a219267668a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with op.batch_alter_table("users") as batch_op:
        batch_op.create_unique_constraint("uq_users_phone",["phone"])


def downgrade() -> None:
    with op.batch_alter_table("users") as batch_op:
        batch_op.drop_constraint("uq_users_phone", type_='unique')
