from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__,
            template_folder='../templates',
            static_folder='../assets',
            static_url_path='/assets')

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqldb://root:root@localhost:3306/pic_learn"
db = SQLAlchemy(app)

from outpg_first.routes import user_pc
from outpg_first.routes import admin_pc

