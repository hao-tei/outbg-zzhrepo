from outpg_first.modules.artical import Artical
from outpg_first.routes import db
from sqlalchemy import Select

class ArticalService:

    def get_Artical(self, id):
        return db.session.get(Artical, id)

    def get_allArticle(self):
        query = Select(Artical)
        return db.session.scalars(query).all()