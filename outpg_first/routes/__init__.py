from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
app = Flask(__name__,
            template_folder='../templates',
            static_folder='../assets',
            static_url_path='/assets')

#db接续
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqldb://root:root@localhost:3306/pic_learn"
db = SQLAlchemy(app)
#登录接续
app.config['SECRET_KEY'] = 'os23di9823v3nge32y'
login_manager = LoginManager(app)

from outpg_first.routes import user_pc
from outpg_first.routes import admin_pc

