from django.db import models
import django.utils.timezone as timezone
from django.contrib.auth.hashers import make_password
from django.utils.translation import ugettext_lazy as _


# Create your models here.

class Users(models.Model):
    # usercode = models.CharField(_('账号'), max_length=130, unique=True, default='', null=True)
    # username = models.CharField(_('用户名'), max_length=130, unique=True, default='', null=True)
    password = models.CharField(_('密码'), max_length=128,
                                help_text=_("Use to make_password or use to reset password form."), null=True)
    email = models.EmailField(_('电子邮件'), max_length=254, unique=True, default='', null=True)
    phone = models.CharField(_('手机号'), max_length=128, unique=True, default='', null=True)

    class Meta:
        managed = True  # False
        verbose_name = _('用户基本信息')
        verbose_name_plural = _('1.用户')
        ordering = ('phone', 'email', 'password')
        db_table = 'users'

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(Users, self).save(*args, **kwargs)

    def set_password(self, raw_password):
        """import random
        algo = 'sha1'
        salt = get_hexdigest(algo, str(random.random()), str(random.random()))[:5]
        hsh = get_hexdigest(algo, salt, raw_password)
        self.password = '%s$%s$%s' % (algo, salt, hsh)"""

    def __str__(self):
        return self.phone

    # def __unicode__(self):
    #     return self.id


class UserInfo(models.Model):
    usercode = models.CharField(_('账号'), max_length=130, unique=True, default='', null=True)
    username = models.CharField(_('用户名'), max_length=130, unique=True, default='', null=True)
    password = models.CharField(_('密码'), max_length=128,
                                help_text=_("Use to make_password or use to reset password form."), null=True)
    gender = models.BooleanField(_('性别'), null=True, default=None, choices=((0, '女'), (1, '男')))
    email = models.EmailField(_('电子邮件'), max_length=254, unique=True, default='', null=True)
    phone = models.CharField(_('手机号'), max_length=128, unique=True, default='', null=True)
    visits = models.IntegerField(_('访问次数'), default=1, blank=True, null=True)
    profile_picture = models.URLField(_('头像文件'), blank=True, null=True)
    is_active = models.BooleanField(_('用户状态'), null=True, default=None, choices=((0, '锁定'), (1, '正常')))
    last_login = models.DateTimeField(_('上次访问时间'), default=timezone.now, null=True)
    date_joined = models.DateTimeField(_('注册时间'), auto_now=True, null=True)

    # user_id = models.OneToOneField("Users", on_delete=models.CASCADE)

    class Meta:
        managed = True  # False
        verbose_name = _('用户详情')
        verbose_name_plural = _('2.用户详情')
        db_table = 'userinfo'

    # def __str__(self):
    #     return str(self.user_id)  # Users.username

