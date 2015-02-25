"""empty message

Revision ID: 4b3d3cfa017d
Revises: 222d18e4aaff
Create Date: 2015-02-10 00:12:29.956054

"""

# revision identifiers, used by Alembic.
revision = '4b3d3cfa017d'
down_revision = '222d18e4aaff'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('item', sa.Column('author_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'item', 'user', ['author_id'], ['id'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'item', type_='foreignkey')
    op.drop_column('item', 'author_id')
    ### end Alembic commands ###
