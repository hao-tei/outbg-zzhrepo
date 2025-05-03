# 
# from flask_login import login_user
# from sqlalchemy import Select
# from outpg_first.modules.users import Users
# from outpg_first.routes import db
# 
# 
# class UserService:
# 
# 
#     def do_login(self, username: str, password: str) -> bool:
#         query = Select(Users).where(Users.name == username)
#         #one_or_none很重要
#         attempted_user = db.session.scalars(query).one_or_none()
#         if attempted_user and attempted_user.check_pass(
#                 attempted_pw=password):
#             login_user(attempted_user)
#             return True
#         return False
