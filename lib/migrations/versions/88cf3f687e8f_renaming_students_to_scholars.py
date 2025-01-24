"""Renaming students to scholars

Revision ID: 88cf3f687e8f
Revises: 791279dd0760
Create Date: 2025-01-24 16:45:09.604496

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '88cf3f687e8f'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table("students", "scholars")


def downgrade() -> None:
    op.rename_table("scholars", "students")
