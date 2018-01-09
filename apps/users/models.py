# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class UserProfile(AbstractUser):
    nickname = models.CharField(max_length=50, verbose_name=u'昵称', default=u'')
    birthday = models.DateField(verbose_name=u'生日', null=True, blank=True)
    gender = models.IntegerField(choices=((0, u'女'), (1, u'男')), verbose_name=u'性别', default=0)
    address = models.CharField(max_length=256, verbose_name=u'地址', null=True, blank=True)
    mobile = models.CharField(max_length=11, verbose_name=u'电话', null=True, blank=True)
    avatar = models.ImageField(max_length=256, upload_to="image/%y/%m", default=u'image/default.png')

    class Meta:
        verbose_name = u'用户信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username
