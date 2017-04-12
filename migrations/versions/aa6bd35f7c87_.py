"""empty message

Revision ID: aa6bd35f7c87
Revises: 2b30b28053ff
Create Date: 2017-04-12 10:12:46.973183

"""

# revision identifiers, used by Alembic.
revision = 'aa6bd35f7c87'
down_revision = '2b30b28053ff'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('uix_1', 'lookaheads', ['project_id', 'reportingdate_id', 'section_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('uix_1', 'lookaheads', type_='unique')
    # ### end Alembic commands ###
