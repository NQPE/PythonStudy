# -*- coding: utf-8 -*-
# __author__= Levi
# __date__= 2018/1/10 15:32

import xadmin

from course.models import Course, Lession, Video, CourseResource


class CourseAdmin(object):
    list_display = ['name', 'desc', 'degree','image', 'learn_times','learn_nums','fav_nums']
    search_fields = ['name', 'desc', 'degree','image', 'learn_times','learn_nums','fav_nums']
    list_filter = ['name', 'desc', 'degree','image', 'learn_times','learn_nums','fav_nums']
    pass


xadmin.site.register(Course, CourseAdmin)

class LessionAdmin(object):
    list_display = ['course', 'name', 'add_time']
    search_fields =  ['course', 'name']
    list_filter =  ['course__name', 'name', 'add_time']
    pass


xadmin.site.register(Lession, LessionAdmin)
