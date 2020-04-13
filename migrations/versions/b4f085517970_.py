"""empty message

Revision ID: b4f085517970
Revises: e45033620f56
Create Date: 2020-03-23 11:10:03.924618

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b4f085517970'
down_revision = 'e45033620f56'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('donations', sa.Column('orgname', sa.String(length=64), nullable=True))
    op.add_column('donations', sa.Column('username', sa.String(length=64), nullable=True))
    op.drop_constraint(None, 'donations', type_='foreignkey')
    op.drop_constraint(None, 'donations', type_='foreignkey')
    op.create_foreign_key(None, 'donations', 'NGO', ['orgname'], ['orgname'])
    op.create_foreign_key(None, 'donations', 'user', ['username'], ['username'])
    op.drop_column('donations', 'user_id')
    op.drop_column('donations', 'org_id')
    op.create_foreign_key(None, 'volunteer', 'NGO', ['related_with'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'volunteer', type_='foreignkey')
    op.add_column('donations', sa.Column('org_id', sa.INTEGER(), nullable=True))
    op.add_column('donations', sa.Column('user_id', sa.INTEGER(), nullable=True))
    op.drop_constraint(None, 'donations', type_='foreignkey')
    op.drop_constraint(None, 'donations', type_='foreignkey')
    op.create_foreign_key(None, 'donations', 'NGO', ['org_id'], ['id'])
    op.create_foreign_key(None, 'donations', 'user', ['user_id'], ['id'])
    op.drop_column('donations', 'username')
    op.drop_column('donations', 'orgname')
    # ### end Alembic commands ###
