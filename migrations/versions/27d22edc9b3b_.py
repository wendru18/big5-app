"""empty message

Revision ID: 27d22edc9b3b
Revises: 4b5c35441ea0
Create Date: 2021-03-08 18:09:23.087620

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '27d22edc9b3b'
down_revision = '4b5c35441ea0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Documents', sa.Column('content', sa.Text(), nullable=True))
    op.drop_column('Documents', 'document')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Documents', sa.Column('document', sa.TEXT(), autoincrement=False, nullable=True))
    op.drop_column('Documents', 'content')
    # ### end Alembic commands ###
