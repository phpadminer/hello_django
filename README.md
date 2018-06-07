# hello_django

### 1.1 开发环境
- [x]  python3.6
- [x]  django1.9.5
> pip install django==1.9.5
- [x]  mysql5.6

- [x]  pymysql0.7.2
> pip install pymysql0.7.2

### 2.1 创建第一个django项目
> 首先执行以下命令创建第一个django项目,中括号里面的项目名称 可以自己定义
```
django-admin startproject [mysite]
```
运行完后会在当前目录中创建一个名为【mysite】的目录！目录的结构如下
```
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        wsgi.py
```
### 2.2 开启简易服务器
> 我们可以运行以下命令来来看起django自带的服务器功能 这样子我们就可以在浏览器中直观的看到我们的这个项目的运行结果！

__【重要提示】__
==必须进入创建的项目的目录中执行，否则会报错！==

```
cd mysite
python manage.py runserver
```
这时候应该会有如下输出：
```
Performing system checks...

System check identified no issues (0 silenced).

You have * unapplied migrations; your app may not work properly until they are applied.
Run 'python manage.py migrate' to apply them.

六月 01, 2018 - 15:50:53
Django version 2.0, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
上面的输出中有
```
You have * unapplied migrations; your app may not work properly until they are applied.
Run 'python manage.py migrate' to apply them.
```
这一部分应该是红色的，我反正是这样子的(osx系统),还有上面的 * 是数字，我显示的是12 每个人出现的情况可能不一样，所以我就用 * 代替！

当然啦，出现红色部分不要害怕！！这不是说你运行失败了！你直接在浏览者访问 [http://127.0.0.1:8000](http://127.0.0.1:8000) 你将会看到一个“祝贺”页面，随着一只火箭发射，服务器已经运行了。看到这个画面说明成功了~

### 2.3 创建一个超级管理员
如果我们这时候访问[http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) 会看到一个登录界面。 需要我们输出用户名和密码 ！然鹅？我们并不知道啊？也没有设置过？咋弄呢！

不要慌，这时候我们就需要来运行以下的命令了：
```
python manage.py createsuperuser
```
这时候会让我们输入用户名、邮箱、密码。这个大家自行这是我就不多说了！如果出现错误的话，就运行之前红色提醒部分的代码
```
python manage.py migrate
```
运行完之后再重新执行上面的创建命令！



