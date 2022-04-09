from flask import session,render_template,current_app, redirect
from . import news_blue

@news_blue.route("/")
def index():
    """
    项目首页加载
    1、使用模板加载项目首页----把static文件夹粘贴到info/目录下

    :return:
    """
    session['itcast'] = '2019'
    return redirect('/static/html/login.html')



