"""empty message

Revision ID: 94b198e20946
Revises: 2fc10c21bf88
Create Date: 2024-07-11 15:19:19.174568

"""

from alembic import op
import sqlalchemy as sa
import sqlmodel.sql.sqltypes
from tidb_vector.sqlalchemy import VectorType


# revision identifiers, used by Alembic.
revision = "94b198e20946"
down_revision = "2fc10c21bf88"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "data_sources",
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=True,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=True,
        ),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sqlmodel.sql.sqltypes.AutoString(length=256), nullable=False),
        sa.Column(
            "description", sqlmodel.sql.sqltypes.AutoString(length=512), nullable=False
        ),
        sa.Column(
            "data_source_type",
            sqlmodel.sql.sqltypes.AutoString(length=256),
            nullable=False,
        ),
        sa.Column("config", sa.JSON(), nullable=True),
        sa.Column("build_kg_index", sa.Boolean(), nullable=False),
        sa.Column("user_id", sqlmodel.sql.sqltypes.GUID(), nullable=True),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "uploads",
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=True,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=True,
        ),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sqlmodel.sql.sqltypes.AutoString(length=255), nullable=False),
        sa.Column("size", sa.Integer(), nullable=False),
        sa.Column("path", sqlmodel.sql.sqltypes.AutoString(length=255), nullable=False),
        sa.Column(
            "mime_type", sqlmodel.sql.sqltypes.AutoString(length=64), nullable=False
        ),
        sa.Column("user_id", sqlmodel.sql.sqltypes.GUID(), nullable=True),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.add_column("documents", sa.Column("data_source_id", sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("documents", "data_source_id")
    op.drop_table("uploads")
    op.drop_table("data_sources")
    # ### end Alembic commands ###