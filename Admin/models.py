from django.contrib.auth.hashers import make_password, check_password
from django.db import models


# Create your models here.


class AdminUser(models.Model):
    a_username = models.CharField(max_length=16, unique=True)
    a_password = models.CharField(max_length=256)
    is_delete = models.BooleanField(default=False)
    is_super = models.BooleanField(default=False)

    # make_password密码加密
    def set_password(self, password):
        self.a_password = make_password(password)

    # 检查密码是否一致check_password(未加密密码，数据库保存的加密密码)
    def check_admin_password(self, password):
        print('---------')
        print(password)
        print(self.a_password)
        return check_password(password, self.a_password)




