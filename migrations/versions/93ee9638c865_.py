"""empty message

Revision ID: 93ee9638c865
Revises: 
Create Date: 2022-08-30 21:02:07.127818

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '93ee9638c865'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('rule_class', sa.Column('cookie', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('rule_class', 'cookie')
    # ### end Alembic commands ###