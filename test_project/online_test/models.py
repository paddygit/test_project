# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Test(models.Model):
    """
        Test's model, works as a wrapper for the questions
    """
    name = models.CharField(max_length=64, verbose_name='Test name')
    slug = models.SlugField(null=True, verbose_name='Test Slug')
    duration = models.FloatField(default=0.0, verbose_name='Test Duration',
                                 help_text='Add duration in minutes only')
    no_of_question = models.IntegerField(default=0,
                                         help_text='This will indicate the '
                                                   'total number of question '
                                                   'consist in a Test')

    def __repr__(self):
        return "{0}".format(self.name)

    def __unicode__(self):
        return self.__repr__()

    class Meta:
        verbose_name = "Test"
        verbose_name_plural = "Tests"


class Question(models.Model):
    """
        Question's Model, which is used as the question for the Test Model
    """
    question_text = models.TextField(max_length=256,
                                     verbose_name='Question')
    test = models.ForeignKey(Test, verbose_name='Test')

    def __repr__(self):
        return "<(Test-{0}) Question {1}>".format(self.test.name,
                                                 self.question_text)

    def __unicode__(self):
        return self.__repr__()

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"


class MultipleChoice(models.Model):
    """
        Multiple Choice's Model, used as the choices for the Question
    """
    choice_text = models.CharField(max_length=128, verbose_name='Choice')
    is_valid = models.BooleanField(default=False,
                                   verbose_name='Is Correct Choice')
    question = models.ForeignKey(Question, verbose_name='Question')

    def __repr__(self):
        return "<(Question-{0}) Choice {1}>".format(
            self.question.question_text, self.choice_text)

    def __unicode__(self):
        return self.__repr__()

    class Meta:
        verbose_name = "Multiple Choice"
        verbose_name_plural = "Multiple Choices"
