"""empty message

Revision ID: 664cce76bbdf
Revises: 14f08af8fa84
Create Date: 2024-05-17 21:33:07.833751

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '664cce76bbdf'
down_revision = '14f08af8fa84'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('media', schema=None) as batch_op:
        batch_op.add_column(sa.Column('task_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'task', ['task_id'], ['id'])

    with op.batch_alter_table('pricing', schema=None) as batch_op:
        batch_op.alter_column('description',
               existing_type=sa.VARCHAR(length=250),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pricing', schema=None) as batch_op:
        batch_op.alter_column('description',
               existing_type=sa.VARCHAR(length=250),
               nullable=True)

    with op.batch_alter_table('media', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('task_id')

    # ### end Alembic commands ###