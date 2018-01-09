# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime

from django.db import models


# Create your models here.
class CityDict(models.Model):
    name = models.CharField(max_length=50, verbose_name=u'城市名称')
    desc = models.CharField(max_length=200, verbose_name=u'城市描述')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'城市'
        verbose_name_plural = verbose_name


class CourseOrg(models.Model):
    name = models.CharField(max_length=50, verbose_name=u'机构名称')
    desc = models.TextField(verbose_name=u'机构描述')
    fav_nums = models.IntegerField(verbose_name=u'收藏人数', default=0)
    click_nums = models.IntegerField(verbose_name=u'机构点击数', default=0)
    image = models.ImageField(upload_to='org/%y/%m', verbose_name=u'封面图片', max_length=256)
    address = models.CharField(max_length=150, verbose_name=u'机构地址')
    city = models.ForeignKey(CityDict, verbose_name=u'城市外键')



