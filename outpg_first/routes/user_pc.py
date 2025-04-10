from outpg_first.forms.login_form import LoginForm
from outpg_first.routes import app
from flask import render_template, abort, redirect, url_for, flash
from outpg_first.services.artical_service import *
from outpg_first.services.users_service import *
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


@app.route("/login.html", methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    # POST+VALIDATE
    if form.validate_on_submit():
        result = UserService().do_login(username=form.username.data, password=form.password.data)
        if result:
            return redirect(url_for("home_page"))
        else:
            flash("error!", category='danger')
    return render_template("login.html", form=form)