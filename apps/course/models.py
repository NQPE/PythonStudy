# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models


# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name=u'课程名称', default=u'')
    desc = models.CharField(max_length=300, verbose_name=u'课程描述', default=u'')
    detail = models.TextField(verbose_name=u'课程详情')
    degree = models.IntegerField(choices=((0, u"初级"), (1, u"中级"), (2, u"高级")), verbose_name=u'课程难度')
    learn_times = models.IntegerField(verbose_name=u'学习时长(分钟数)', default=0)
    learn_nums = models.IntegerField(verbose_name=u'学习人数', default=0)
    fav_nums = models.IntegerField(verbose_name=u'收藏人数', default=0)
    image = models.ImageField(upload_to='courses/%y/%m', verbose_name=u'封面图片', max_length=256)
    click_nums = models.IntegerField(verbose_name=u'课程点击数', default=0)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'课程'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name

class Lession(models.Model):
    course = models.ForeignKey(Course, verbose_name=u'课程')
    name = models.CharField(max_length=100, verbose_name=u'章节名称', default=u'')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'章节'
        verbose_name_plural = verbose_name


class Video(models.Model):
    lession = models.ForeignKey(Lession, verbose_name=u'章节')
    name = models.CharField(max_length=100, verbose_name=u'视频名称', default=u'')
    url = models.CharField(max_length=256, verbose_name=u'视频链接', default=u'')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'视频'
        verbose_name_plural = verbose_name


class CourseResource(models.Model):
    course = models.ForeignKey(Course, verbose_name=u'课程')
    name = models.CharField(max_length=100, verbose_name=u'资源名称', default=u'')
    download = models.FileField(upload_to='courses/resource/%y/%m',max_length=256, verbose_name=u'资源链接', default=u'')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'课程资源'
        verbose_name_plural = verbose_name
