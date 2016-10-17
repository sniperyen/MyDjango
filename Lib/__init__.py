# coding:utf-8

# 扩展的第三方app放到此目录，其他地方引用时，从这里引用
#
# 我推荐一种简单的方法来解决这个问题，以easy_thumbnails 为例：
#
# 1、假设您的项目在c:\test,在你的项目里面建一个Lib文件夹（名称你可以自己取）
#
# 2、将python\\Lib\site-packages里面的easy_thumbnails文件夹复制到Lib文件夹.
#
# 3、将INSTALLED_APP里面的easy_thumbnails ，更改为 Lib.easy_thumbnails
#
# 4、接下来，将easy_thumbnails 文件夹里面所有用到from xxx   import  xxxx的地方更改为相对import，以确保easy_thumbnails 自身能正确import
#
# ，这一步很关键，我发现不少app均是采用全局import方式，如果不改会发生import错误。
#
# 5、最后在其他有用到easy_thumbnails 的地方，均从新位置import.