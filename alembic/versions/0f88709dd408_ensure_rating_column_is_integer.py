"""Ensure rating column is Integer

Revision ID: 0f88709dd408
Revises: c9919f5b9234
Create Date: 2024-11-23 14:37:18.584286

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0f88709dd408'
down_revision: Union[str, None] = 'c9919f5b9234'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###