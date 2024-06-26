"""Add fields for gateways behind ALB

Revision ID: dfffd6a1165c
Revises: c154eece89da
Create Date: 2024-05-22 13:38:18.322032

"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "dfffd6a1165c"
down_revision = "c154eece89da"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("gateway_computes", schema=None) as batch_op:
        batch_op.add_column(sa.Column("hostname", sa.String(length=100), nullable=True))
        batch_op.add_column(sa.Column("configuration", sa.Text(), nullable=True))
        batch_op.add_column(sa.Column("backend_data", sa.Text(), nullable=True))

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("gateway_computes", schema=None) as batch_op:
        batch_op.drop_column("backend_data")
        batch_op.drop_column("configuration")
        batch_op.drop_column("hostname")

    # ### end Alembic commands ###
