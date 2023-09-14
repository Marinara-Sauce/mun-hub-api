"""added stuff

Revision ID: 660eaf3ea5fe
Revises: 98cfc44718de
Create Date: 2023-09-14 18:47:37.534105

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '660eaf3ea5fe'
down_revision: Union[str, None] = '98cfc44718de'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
