"""settings-base-conf

Revision ID: 115f628e1d03
Revises: 364cfff3dd87
Create Date: 2024-11-02 21:20:36.474107

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '115f628e1d03'
down_revision: Union[str, None] = '364cfff3dd87'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute(
        '''
        INSERT INTO settings (dynamic_button_count, welcome_message)
        VALUES (2, '🤖 {{NAME}} ({{USERNAME}})...connecting to «IT Lobby Irkutsk». Вошёл, за своё aйти пояснил. Программист, инженер, робототехник, сис.админ или каким-то образом связан с IT и технологиями, то расскажи о себе и своей деятельности.')
        '''
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute('DELETE FROM settings WHERE id = 1')
    # ### end Alembic commands ###
