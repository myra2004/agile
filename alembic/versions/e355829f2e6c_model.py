"""model

Revision ID: e355829f2e6c
Revises: e9a36275a759
Create Date: 2025-07-24 13:43:37.439496

"""

from collections.abc import Sequence

# revision identifiers, used by Alembic.
revision: str = "e355829f2e6c"
down_revision: str | Sequence[str] | None = "e9a36275a759"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
