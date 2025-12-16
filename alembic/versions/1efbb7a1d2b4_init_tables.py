"""init tables

Revision ID: 1efbb7a1d2b4
Revises: 
Create Date: 2025-08-19

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1efbb7a1d2b4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('username', sa.String, nullable=False, unique=True, index=True),
        sa.Column('email', sa.String, nullable=False, unique=True, index=True),
        sa.Column('password', sa.String, nullable=False),
    )

    op.create_table(
        'profiles',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id', ondelete="CASCADE")),
        sa.Column('full_name', sa.String, nullable=False),
        sa.Column('bio', sa.String, nullable=True),
    )

    op.create_table(
        'subscriptions',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id', ondelete="CASCADE")),
        sa.Column('plan', sa.String, nullable=False),
        sa.Column('is_active', sa.Boolean, default=True),
    )

    op.create_table(
        'pos_modules',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('name', sa.String, nullable=False, unique=True),
        sa.Column('description', sa.String, nullable=True),
    )


def downgrade() -> None:
    op.drop_table('pos_modules')
    op.drop_table('subscriptions')
    op.drop_table('profiles')
    op.drop_table('users')
