# 将整个网页都设置为可在前端自定义修改，个性化设置

from flask import render_template, request, flash
from flask_login import login_required

from miniblog.app import app
from miniblog.models import PersonalSetting


ps = PersonalSetting()


@app.route("/admin")
@login_required
def admin():
    return render_template("admin/manage_home.html")


@app.route("/upload")
def md_upload():
    pass


@app.route("/modify_webtitle", methods=["GET", "POST"])
@login_required
def modify_webtitle():
    new_webtitle = request.form.get("webtitle")
    if new_webtitle == ps.get_webtitle:
        flash("请尝试输入不同的标题！")
        return render_template("admin/manage_home.html")
    ps.modify_webtitle(new_webtitle)
    flash("修改成功，新标题为：" + str(new_webtitle) + "，你可以返回主页进行查看！")
    return render_template("admin/manage_home.html")


@app.route("/modify_websignature", methods=["GET", "POST"])
@login_required
def modify_websignature():
    new_websignature = request.form.get("websignature")
    if new_websignature == ps.get_websignature:
        flash("请尝试输入不同的网站签名！")
        return render_template("admin/manage_home.html")
    ps.modify_websignature(new_websignature)
    flash("修改成功，新网站签名为：" + str(new_websignature) + "，你可以返回主页进行查看！")
    return render_template("admin/manage_home.html")


@app.route("/modify_nickname", methods=["GET", "POST"])
@login_required
def modify_nickname():
    new_nickname = request.form.get("nickname")
    if new_nickname == ps.get_nickname:
        flash("请尝试输入不同的个人昵称！")
        return render_template("admin/manage_home.html")
    ps.modify_nickname(new_nickname)
    flash("修改成功，新个人昵称为：" + str(new_nickname) + "，你可以返回主页进行查看！")
    return render_template("admin/manage_home.html")


@app.route("/modify_signature", methods=["GET", "POST"])
@login_required
def modify_signature():
    new_signature = request.form.get("signature")
    if new_signature == ps.get_signature:
        flash("请尝试输入不同的个性签名！")
        return render_template("admin/manage_home.html")
    ps.modify_signature(new_signature)
    flash("修改成功，新个性签名为：" + str(new_signature) + "，你可以返回主页进行查看！")
    return render_template("admin/manage_home.html")


@app.route("/modify_statement", methods=["GET", "POST"])
@login_required
def modify_statement():
    new_statement = request.form.get("statement")
    if new_statement == ps.get_statement:
        flash("请尝试输入不同的技术栈说明！")
        return render_template("admin/manage_home.html")
    ps.modify_statement(new_statement)
    flash("修改成功，新技术栈说明为：" + str(new_statement) + "，你可以返回主页进行查看！")
    return render_template("admin/manage_home.html")


@app.route("/append_tech_web", methods=["GET", "POST"])
@login_required
def append_tech_web():
    new_title = request.form.get("title")
    new_url = request.form.get("url")
    ps.append_techweb(new_title, new_url)
    flash("添加成功，新技术网站为：" + str(new_title) + "，网址为：" + str(new_url) + "，你可以返回主页进行查看！")
    return render_template("admin/manage_home.html")


@app.route("/append_other_web", methods=["GET", "POST"])
@login_required
def append_other_web():
    new_title = request.form.get("title")
    new_url = request.form.get("url")
    ps.append_otherweb(new_title, new_url)
    flash("添加成功，新其他网站为：" + str(new_title) + "，网址为：" + str(new_url) + "，你可以返回主页进行查看！")
    return render_template("admin/manage_home.html")


@app.route("/append_note_doc", methods=["GET", "POST"])
@login_required
def append_note_doc():
    new_title = request.form.get("title")
    new_url = request.form.get("url")
    ps.append_notedoc(new_title, new_url)
    flash("添加成功，新笔记文档为：" + str(new_title) + "，网址为：" + str(new_url) + "，你可以返回主页进行查看！")
    return render_template("admin/manage_home.html")


@app.route("/append_code_note", methods=["GET", "POST"])
@login_required
def append_code_note():
    new_title = request.form.get("title")
    new_url = request.form.get("url")
    ps.append_codenote(new_title, new_url)
    flash("添加成功，新代码笔记为：" + str(new_title) + "，网址为：" + str(new_url) + "，你可以返回主页进行查看！")
    return render_template("admin/manage_home.html")


@app.route("/append_myproject", methods=["GET", "POST"])
@login_required
def append_myproject():
    new_title = request.form.get("title")
    new_url = request.form.get("url")
    ps.append_myproject(new_title, new_url)
    flash("添加成功，新原创项目为：" + str(new_title) + "，网址为：" + str(new_url) + "，你可以返回主页进行查看！")
    return render_template("admin/manage_home.html")


@app.route("/append_rebook", methods=["GET", "POST"])
@login_required
def append_rebook():
    new_title = request.form.get("title")
    new_url = request.form.get("url")
    ps.append_recommandbook(new_title, new_url)
    flash("添加成功，新推荐书籍为：" + str(new_title) + "，网址为：" + str(new_url) + "，你可以返回主页进行查看！")
    return render_template("admin/manage_home.html")
