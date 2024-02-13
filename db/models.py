from tortoise import fields
from tortoise.models import Model
from tortoise import Tortoise, run_async


# 心愿呈现
class User(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=32, null=True, description="用户名", default="root")
    email = fields.CharField(max_length=128, null=True, description="邮箱")
    age = fields.IntField(null=True, description="年龄")
    birthday = fields.DateField(null=True, description="生日")
    user_scl = fields.CharField(max_length=256, null=True, description="用户头像URL")
    create_time = fields.DateField(null=True, description="注册时间", auto_now_add=True)
    password = fields.CharField(max_length=32, null=True, description="密码")

    # 心愿关联 | 反向查询
    user_to_wish = fields.ManyToManyField("models.Wish", related_name="user_to_wish")

    def __str__(self):
        return self.name


class Wish(Model):
    wish_id = fields.IntField()
    wish_title = fields.TextField(null=True, description="标题")
    wish_content = fields.TextField(null=True, description="内容")
    wish_area = fields.CharField(max_length=32, null=True, description="记录地区")

    def __str__(self):
        return self.wish_title


class UserDetail(Model):
    bio = fields.TextField(description="用户简介")
    address = fields.CharField(max_length=256, null=True, description="居住地")
    school = fields.CharField(max_length=256, description="毕业学院", null=True)
    user = fields.ForeignKeyField("models.User", related_name="user_detail")

    def __str__(self):
        return self.bio


# 用户上传的心愿图片表
class UserAvatar(Model):
    avatar_id = fields.IntField()
    user = fields.ForeignKeyField("models.User", related_name="user_avatar")
    image = fields.BinaryField(null=True, description="图片")

    def __str__(self):
        return f'用户{self.user}的图片'

