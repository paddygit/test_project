# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from online_test.models import MultipleChoice
from rest_framework import serializers
# Create your models here.


# class UserResult(models.Model):
#     """
#         UserResult's model, works as a result for the test
#     """
#     correct_answer = models.IntegerField(default=0)
#     wrong_answer = models.IntegerField(default=0)
#     final_score = models.IntegerField(default=0)
#     registration = models.ForeignKey(User)
#     test = models.ForeignKey(Test)
#
#     def __str__(self):
#         return self.registration.username


class UserAnswers(models.Model):
    """
        User Answers's model, works as a wrapper for the User Result
    """
    user = models.ForeignKey(User, null=True)
    answer = models.ForeignKey(MultipleChoice, verbose_name="Answer",
                               null=True)

    def save(self, *args, **kwargs):
        # overridding save
        if not self.pk:
            if UserAnswers.objects.filter(
                    answer__question=self.answer.question, user=self.user):
                raise serializers.ValidationError(
                    'You have already given the answer'
                )
        super(UserAnswers, self).save(*args, **kwargs)

    def __repr__(self):
        return "<{0}>".format(self.user)

    def __unicode__(self):
        return self.__repr__()

    class Meta:
        verbose_name = "User Answer"
        verbose_name_plural = "User Answers"
