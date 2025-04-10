from flask_login import UserMixin
from outpg_first.routes import db
from datetime import datetime
from sqlalchemy import Integer, String, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column
from outpg_first.routes import login_manager

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(Users, user_id)

#UserMixin中有些额外的方法
class Users(db.Model, UserMixin):

    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    password: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False)
    cre_time: Mapped[datetime] = mapped_column(TIMESTAMP, nullable=False)
    upd_time: Mapped[datetime] = mapped_column(TIMESTAMP, nullable=False)
    del_flg: Mapped[int] = mapped_column(Integer, nullable=False)

    def check_pass(self, attempted_pw):
        return self.password == attempted_pw

