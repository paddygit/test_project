# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import filters
from result.models import UserAnswers
from rest_framework.permissions import IsAuthenticated
from drf_custom_viewsets.viewsets import CustomSerializerViewSet
from result.serializers import GetUserAnswersSerializer, PostUserAnswersSerializer


class UserAnswersViewSet(CustomSerializerViewSet):
    """
        API endpoint that allows user-answers to be viewed or edited.
    """
    permission_classes = (IsAuthenticated,)
    queryset = UserAnswers.objects.all()
    serializer_class = GetUserAnswersSerializer
    custom_serializer_classes = {
        'create': PostUserAnswersSerializer,
        'update': PostUserAnswersSerializer,
    }
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = {
        'user__username': ['exact'],
        'answer__question__test__slug': ['exact'],
        'answer__is_valid': ['exact']
    }
