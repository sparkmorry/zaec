需要安装的Python框架／库：

$pip install Flask

$pip install Flask-Peewee


1. 先在本地数据库创建表zaec，按utf8编码形式（重要！）

create database zaec DEFAULT CHARACTER SET utf8;

2. 运行main.py文件即可

再打开127.0.0.1:5000

3. 管理员入口为127.0.0.1:5000/admin

需要用户名和密码，现在设定为admin，密码123456，关于权限设置主要在auth.py文件中

4. 几个文件的主要作用：

config.py：设置数据库配置及几个URL路径

app.py：创建flask应用及数据库

auth.py：管理权限的设置

admin.py：管理入口相关设置，需要的几个控制页面的模型

models.py：用了peewee-orm，2个主要数据模型的创建

view.py：视图函数，主要处理url

main.py：运行
