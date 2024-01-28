import click

from miniblog.app import app, db
from miniblog.models import Admin


@app.cli.command()
@click.option("--drop", is_flag=True, help="Create after drop")
def init_db(drop):
    """初始化数据库"""
    if drop:
        click.confirm("此操作将会删除数据库, 是否继续？", abort=True)
        db.drop_all()
        click.echo("已删除")
    db.create_all()
    click.echo("初始化数据库")


@app.cli.command()
@click.option("--username", prompt=True, help="用户登录名称")
@click.option("--password", prompt=True, confirmation_prompt=True, help="用户登录密码")
def init_admin(username, password):
    """建立管理员账户以及默认分类"""
    click.echo("正在初始化数据库...")
    db.create_all()

    admin = Admin.query.first()
    if admin is not None:
        click.echo("此管理员已存在, 更新ing...")
        admin.username = username
        admin.set_password(password)
    else:
        click.echo("创建管理员账户...")
        admin = Admin(username=username)
        admin.set_password(password)
        db.session.add(admin)

    db.session.commit()
    click.echo("创建完成")
