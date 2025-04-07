from outpg_first.routes import app
from flask import render_template, abort
from outpg_first.services.artical_service import *
@app.route("/")
@app.route("/index.html")
def home_page():
    articles = ArticalService().get_allArticle()
    return render_template("index.html", articles=articles)

@app.route("/article/<article_id>.html")
def article_page(article_id):
    article = ArticalService().get_Artical(article_id)
    if article:
        return render_template("article.html", article=article)

    #退出
    abort(404)


@app.route("/login.html")
def login_page():
    return render_template("login.html", my_title="home")