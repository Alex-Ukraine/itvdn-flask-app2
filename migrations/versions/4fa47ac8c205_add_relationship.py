"""add relationship

Revision ID: 4fa47ac8c205
Revises: 26a49978fff9
Create Date: 2021-04-28 04:03:24.730733

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '4fa47ac8c205'
down_revision = '26a49978fff9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('movies_actors',
                    sa.Column('actor_id', sa.Integer(), nullable=False),
                    sa.Column('film_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['actor_id'], ['actors.id'], ),
                    sa.ForeignKeyConstraint(['film_id'], ['films.id'], ),
                    sa.PrimaryKeyConstraint('actor_id', 'film_id')
                    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('movies_actors')
    # ### end Alembic commands ###
