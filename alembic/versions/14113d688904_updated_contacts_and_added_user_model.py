"""Updated contacts and added user model

Revision ID: 14113d688904
Revises: b39827657267
Create Date: 2025-04-03 13:38:40.606799

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '14113d688904'
down_revision: Union[str, None] = 'b39827657267'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('contacts_birth_date_key', 'contacts', type_='unique')
    op.drop_constraint('contacts_first_name_key', 'contacts', type_='unique')
    op.drop_constraint('contacts_last_name_key', 'contacts', type_='unique')
    op.drop_constraint('contacts_phone_number_key', 'contacts', type_='unique')
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('contacts_phone_number_key', 'contacts', ['phone_number'])
    op.create_unique_constraint('contacts_last_name_key', 'contacts', ['last_name'])
    op.create_unique_constraint('contacts_first_name_key', 'contacts', ['first_name'])
    op.create_unique_constraint('contacts_birth_date_key', 'contacts', ['birth_date'])
    # ### end Alembic commands ###
