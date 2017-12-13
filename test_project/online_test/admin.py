# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import *


class MultipleChoiceInline(admin.StackedInline):
    model = MultipleChoice
    extra = 4


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields': ['question_text', 'test']}),
    ]
    inlines = [MultipleChoiceInline]
admin.site.register(Question, QuestionAdmin)

admin.site.register(Test)
admin.site.register(MultipleChoice)
