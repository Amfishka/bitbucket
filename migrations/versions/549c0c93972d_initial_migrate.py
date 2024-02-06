"""Initial migrate

Revision ID: 549c0c93972d
Revises: 
Create Date: 2024-02-02 20:41:51.062814

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '549c0c93972d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('requisites',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('full_name', sa.String(length=150), nullable=False),
    sa.Column('type_payment', sa.String(length=100), nullable=False),
    sa.Column('type_card_or_account', sa.String(length=100), nullable=False),
    sa.Column('number_phone', sa.Integer(), nullable=False),
    sa.Column('limit', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('password', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('request_payment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('summ', sa.Float(), nullable=False),
    sa.Column('requisites', sa.Integer(), nullable=True),
    sa.Column('status', sa.String(length=100), nullable=False),
    sa.ForeignKeyConstraint(['requisites'], ['requisites.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('request_payment')
    op.drop_table('user')
    op.drop_table('requisites')
    # ### end Alembic commands ###
