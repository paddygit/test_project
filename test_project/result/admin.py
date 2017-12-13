# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import *

# Register your models here.


# class UserResultAdmin(admin.ModelAdmin):
#     list_display = ['registration', 'test', 'correct_answer', 'wrong_answer',
#                     'final_score']
#     #search_fields = ['result__user__username']
#
# admin.site.register(UserResult, UserResultAdmin)


class UserAnswerAdmin(admin.ModelAdmin):
    list_display = ['user', 'answer']
    search_fields = ['user__username']

admin.site.register(UserAnswers, UserAnswerAdmin)
