"""empty message

Revision ID: c0e5f75ecc72
Revises: 267fae651421
Create Date: 2022-04-12 17:07:21.316809

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c0e5f75ecc72'
down_revision = '267fae651421'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('itunes_data',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('kind', sa.String(length=255), nullable=False),
    sa.Column('collectionName', sa.String(length=255), nullable=False),
    sa.Column('trackName', sa.String(length=255), nullable=False),
    sa.Column('collectionPrice', sa.Float(), nullable=True),
    sa.Column('trackPrice', sa.Float(), nullable=True),
    sa.Column('primaryGenreName', sa.String(length=255), nullable=False),
    sa.Column('trackCount', sa.Integer(), nullable=True),
    sa.Column('trackNumber', sa.Integer(), nullable=True),
    sa.Column('releaseDate', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('itunes_data')
    # ### end Alembic commands ###
