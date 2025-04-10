from outpg_first.routes import db
from datetime import datetime
from sqlalchemy import Integer, String, BLOB, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column
class Artical(db.Model):
    __tablename__ = 'artical'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    # __ private
    __content: Mapped[bytes] = mapped_column(BLOB, name="content")
    cre_time: Mapped[datetime] = mapped_column(TIMESTAMP, nullable=False)
    upd_time: Mapped[datetime] = mapped_column(TIMESTAMP, nullable=False)
    del_flg: Mapped[int] = mapped_column(Integer, nullable=False)
    @property
    def content(self):
        return self.__content.decode('utf-8')
