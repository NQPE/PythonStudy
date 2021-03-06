# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class UserProfile(AbstractUser):
    nickname = models.CharField(max_length=50, verbose_name=u'昵称', default=u'')
    birthday = models.DateField(verbose_name=u'生日', null=True, blank=True)
    gender = models.IntegerField(choices=((0, u'女'), (1, u'男')), verbose_name=u'性别', default=0)
    address = models.CharField(max_length=256, verbose_name=u'地址', null=True, blank=True)
    mobile = models.CharField(max_length=11, verbose_name=u'电话', null=True, blank=True)
    avatar = models.ImageField(verbose_name=u'头像地址',max_length=256, upload_to="images/%y/%m", default=u'images/default.png')

    class Meta:
        verbose_name = u'用户'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username


class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20, verbose_name=u'验证码')
    email = models.CharField(max_length=254, verbose_name=u'邮箱')
    send_type = models.IntegerField(choices=((0, "注册"), (1, "忘记密码")), verbose_name=u'验证码类型')
    send_time = models.DateTimeField(default=datetime.now, verbose_name=u'发送时间')

    class Meta:
        verbose_name = u'邮箱验证码'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return '{0}({1})'.format(self.code,self.email)


class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name=u'标题')
    image = models.ImageField(upload_to="banner/%y/%m", verbose_name=u'轮播图片')
    url = models.CharField(max_length=254, verbose_name=u'访问地址')
    index = models.IntegerField(default=100, verbose_name=u'顺序')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'轮播图'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title
