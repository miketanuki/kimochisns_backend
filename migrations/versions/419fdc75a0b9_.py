"""empty message

Revision ID: 419fdc75a0b9
Revises: 65b49d694a59
Create Date: 2023-07-09 01:49:11.991462

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '419fdc75a0b9'
down_revision = '65b49d694a59'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.drop_column('sentiment_label')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.add_column(sa.Column('sentiment_label', sa.VARCHAR(length=20), nullable=False))

    # ### end Alembic commands ###