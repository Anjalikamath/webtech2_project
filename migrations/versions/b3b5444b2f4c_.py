"""empty message

Revision ID: b3b5444b2f4c
Revises: 4ad28ab9cc22
Create Date: 2020-03-23 13:31:39.321960

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b3b5444b2f4c'
down_revision = '4ad28ab9cc22'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'donations', type_='foreignkey')
    op.drop_constraint(None, 'donations', type_='foreignkey')
    op.create_foreign_key(None, 'donations', 'user', ['username'], ['username'])
    op.create_foreign_key(None, 'donations', 'NGO', ['orgname'], ['orgname'])
    op.drop_column('donations', 'org_id')
    op.drop_column('donations', 'user_id')
    op.create_foreign_key(None, 'volunteer', 'NGO', ['related_with'], ['orgname'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'volunteer', type_='foreignkey')
    op.add_column('donations', sa.Column('user_id', sa.INTEGER(), nullable=True))
    op.add_column('donations', sa.Column('org_id', sa.INTEGER(), nullable=True))
    op.drop_constraint(None, 'donations', type_='foreignkey')
    op.drop_constraint(None, 'donations', type_='foreignkey')
    op.create_foreign_key(None, 'donations', 'NGO', ['org_id'], ['id'])
    op.create_foreign_key(None, 'donations', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###
