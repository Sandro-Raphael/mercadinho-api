from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from database.database import Base


class Item(Base):
    __tablename__ = "items"

    item_id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    item_name: Mapped[str] = mapped_column(
        String(150),
        nullable=False
    )

    quantity: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=0
    )