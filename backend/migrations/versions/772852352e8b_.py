"""empty message

Revision ID: 772852352e8b
Revises: fb9d1de93735
Create Date: 2024-03-13 11:40:41.833176

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '772852352e8b'
down_revision = 'fb9d1de93735'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('transaction', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created_at', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('updated_at', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('transaction', schema=None) as batch_op:
        batch_op.drop_column('updated_at')
        batch_op.drop_column('created_at')

    # ### end Alembic commands ###
