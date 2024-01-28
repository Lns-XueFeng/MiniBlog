import os
import warnings

from markdown import markdown
from markupsafe import Markup, escape
from flask import render_template, redirect, url_for, flash, g
from flask_login import logout_user, login_user, login_required

from miniblog.app import app, miniblog_absdir, db
from miniblog.forms import LoginForm, CkEditorForm
from miniblog.models import Admin, Passage, PersonalSetting
from miniblog.spider import offer_finally_data


class SpidersFailed(Exception):
    pass


class MarkdownNoToc(Exception):
    pass


@app.before_request
def set_some_global_var():
    ps = PersonalSetting()
    g.webtitle = ps.get_webtitle
    g.websignature = ps.get_websignature
    g.nickname = ps.get_nickname
    g.signature = ps.get_signature
    g.statement = ps.get_statement
    g.techweb = ps.get_techweb
    g.otherweb = ps.get_otherweb


@app.route("/")
def home():
    ps = PersonalSetting()
    md_notes = ps.get_notedoc
    code_notes = ps.get_codenote
    self_projects = ps.get_myproject
    love_books = ps.get_recommandbook
    return render_template(
        "blog/home.html",
        HOME_MD_NOTES=md_notes,
        HOME_CODE_NOTES=code_notes,
        HOME_SELF_PROJECTS=self_projects,
        HOME_LOVE_BOOKS=love_books,
    )


@app.route("/passages")
def passages():
    try:
        PASSAGE_PY, PASSAGE_WEB, PASSAGE_SPIDER, PASSAGE_DISCUSS = offer_finally_data()
        flash("获取公众号文章成功，频繁刷新此页面可能会导致显示失败！")
    except Exception:
        warnings.warn("not expect way to get passage url...")
        flash("获取公众号文章失败，请稍后重试！")
        PASSAGE_PY, PASSAGE_WEB, PASSAGE_SPIDER, PASSAGE_DISCUSS = {}, {}, {}, {}
        raise SpidersFailed
    
    return render_template(
        "blog/passages.html",
        PASSAGE_WEB=PASSAGE_WEB,
        PASSAGE_PY=PASSAGE_PY,
        PASSAGE_SPIDER=PASSAGE_SPIDER,
        PASSAGE_DISCUSS=PASSAGE_DISCUSS
    )


@app.route("/about")
def about():
    return render_template("blog/about.html")


def md_to_html(filename):
    exts = ["markdown.extensions.extra", "markdown.extensions.codehilite",
            "markdown.extensions.tables", "markdown.extensions.toc"]

    with open(filename, 'r', encoding="utf-8") as f:
        md_content = f.read()

    content = markdown(md_content, extensions=exts)
    html = Markup(content)
    return html


@app.route("/md_notes/<name>")
def md_notes(name):
    relative_path = "static/markdown/{}.md".format(name)
    md_abspath = os.path.join(miniblog_absdir, relative_path)
    html_string = md_to_html(md_abspath)
    if '<div class="toc">' in html_string:
        two_part = html_string.split("</div>", maxsplit=2)
        html_toc, html_content = two_part[0] + Markup("</div>"), two_part[1]
        return render_template("blog/show_notes.html", toc=html_toc, content=html_content)
    raise MarkdownNoToc("markdown file no toc")


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        admin = Admin.query.first()
        print(admin.username, admin.validate_password(password))
        if admin:
            if username == admin.username \
                    and admin.validate_password(password):
                login_user(admin)
                flash("登录成功！")
                return redirect(url_for("home"))
            else:
                flash("登录失败！")
        else:
            flash("用户不存在！")
    return render_template("auth/login.html", form=form)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("你已退出登录！")
    return redirect(url_for("home"))


@app.route("/register", methods=["GET", "POST"])
def register():
    pass


@app.route("/passages/new", methods=["GET", "POST"])
@login_required
def new_passage():
    form = CkEditorForm()
    if form.validate_on_submit():
        title = form.title.data
        create_time = form.create_time.data
        text = form.text_field.data
        passage = Passage()
        passage.title, passage.create_time, passage.text = title, create_time, text
        db.session.add(passage)
        db.session.commit()
        flash("成功创建新随记！")
        return redirect(url_for("inner_passages"))
    return render_template("admin/new_passage.html", form=form)


@app.route("/inner_passages")
def inner_passages():
    data = []
    passage_data = Passage.query.all()
    for passage in passage_data:
        passage.text = passage.text.replace("<p>", "")
        passage.text = passage.text.replace("</p>", "")
        passage.text = escape(passage.text)
        data.insert(0, passage)
    return render_template("blog/inner_passages.html", data=data)
