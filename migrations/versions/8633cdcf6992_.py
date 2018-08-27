"""empty message

Revision ID: 8633cdcf6992
Revises: a0c12001e6b2
Create Date: 2018-08-27 17:37:26.719596

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8633cdcf6992'
down_revision = 'a0c12001e6b2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_tasks_name', table_name='tasks')
    op.drop_table('tasks')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tasks',
    sa.Column('id', sa.VARCHAR(length=36), nullable=False),
    sa.Column('name', sa.VARCHAR(length=128), nullable=True),
    sa.Column('description', sa.VARCHAR(length=128), nullable=True),
    sa.Column('url_id', sa.INTEGER(), nullable=True),
    sa.Column('complete', sa.BOOLEAN(), nullable=True),
    sa.CheckConstraint('complete IN (0, 1)'),
    sa.ForeignKeyConstraint(['url_id'], ['URL.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_tasks_name', 'tasks', ['name'], unique=False)
    # ### end Alembic commands ###
