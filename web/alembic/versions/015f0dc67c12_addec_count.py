"""addec count

Revision ID: 015f0dc67c12
Revises: 2e3e21eadeaa
Create Date: 2018-12-02 13:39:37.098688

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '015f0dc67c12'
down_revision = '2e3e21eadeaa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('doplnek_vypujcka', sa.Column('pocet', sa.Integer(), nullable=True))
    op.add_column('vypujcka_kostym', sa.Column('pocet', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('vypujcka_kostym', 'pocet')
    op.drop_column('doplnek_vypujcka', 'pocet')
    # ### end Alembic commands ###
