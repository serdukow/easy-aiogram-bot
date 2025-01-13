"""initial migration

Revision ID: 2cbca5ea5ca1
Revises: 
Create Date: 2025-01-14 00:06:39.044228

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '2cbca5ea5ca1'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('telegram_id', sa.BIGINT(), autoincrement=False, nullable=False),
    sa.Column('full_name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('username', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('is_premium', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('is_bot', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('language', sa.VARCHAR(length=5), autoincrement=False, nullable=False),
    sa.Column('id', sa.BIGINT(), autoincrement=True, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=False),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='pk_users')
    )
    # ### end Alembic commands ###