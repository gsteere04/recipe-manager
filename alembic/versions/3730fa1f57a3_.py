""" drop unused columns of the user table.  (password, email)

Revision ID: 3730fa1f57a3
Revises: c8eec2ecf713
Create Date: 2024-05-15 11:11:54.053549

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3730fa1f57a3'
down_revision: Union[str, None] = 'c8eec2ecf713'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('recipes', sa.Column('instructions', sa.String(), nullable=True))
    op.create_index(op.f('ix_recipes_instructions'), 'recipes', ['instructions'], unique=False)
    op.drop_index('ix_users_email', table_name='users')
    op.drop_column('users', 'password')
    op.drop_column('users', 'email')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('password', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.create_index('ix_users_email', 'users', ['email'], unique=True)
    op.drop_index(op.f('ix_recipes_instructions'), table_name='recipes')
    op.drop_column('recipes', 'instructions')
    # ### end Alembic commands ###
