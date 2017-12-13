# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required
from online_test.models import Test, Question, MultipleChoice
from drf_custom_viewsets.viewsets import CustomSerializerViewSet
from online_test.serializers import UserSerializer, TestSerializer, \
    GetQuestionSerializer, PostQuestionSerializer, \
    GetMultipleChoiceSerializer, PostMultipleChoiceSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('id', 'username', 'email', 'first_name', 'last_name', )


class TestViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tests to be viewed or edited.
    """
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = {
        'slug': ['exact'],
    }


class QuestionViewSet(CustomSerializerViewSet):
    """
    API endpoint that allows questions to be viewed or edited.
    """
    permission_classes = (IsAuthenticated,)
    queryset = Question.objects.all()
    serializer_class = GetQuestionSerializer
    custom_serializer_classes = {
        'create': PostQuestionSerializer,
        'update': PostQuestionSerializer,
    }
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = {
        'test__slug': ['exact'],
    }


class MultipleChoiceViewSet(CustomSerializerViewSet):
    """
    API endpoint that allows multiple choices to be viewed or edited.
    """
    permission_classes = (IsAuthenticated,)
    queryset = MultipleChoice.objects.all()
    serializer_class = GetMultipleChoiceSerializer
    custom_serializer_classes = {
        'create': PostMultipleChoiceSerializer,
        'update': PostMultipleChoiceSerializer,
    }
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = {
        'id': ['exact'],
    }

@login_required(login_url='/login/')
def home_page(request):
    return render(request, 'online_test/test_choose_page.html')


@login_required(login_url='/login/')
def test_paper(request, test_paper_slug):
    return render(request, 'online_test/test_instruction.html',
                  {'test_paper_slug':test_paper_slug,})


@login_required(login_url='/login/')
def test_start(request, test_paper_slug):
    return render(request, 'online_test/test_paper.html',
                  {'test_paper_slug': test_paper_slug})

@login_required(login_url='/login/')
def test_result(request, test_paper_slug):
    return render(request, 'online_test/result.html',
                  {'test_paper_slug': test_paper_slug})


# class QuestionChoicesCustomAPI(generics.ListAPIView):
#     """
#        Custom API for getting Question and Multiple Choices together.
#     """
#     permission_classes = (IsAuthenticated,)
#
#     def get(self, request):
#         get_data = request.query_params
#         all_question = Question.objects.filter(
#             test__slug=get_data['test__slug']
#         )
#         question_list_with_choices = [
#             {
#                 'choices': [
#                     {
#                         'choice_id':  j.id,
#                         'choice_text': j.choice_text
#                     }
#                     for j in MultipleChoice.objects.filter(question__id=i.id)],
#                 'question_id': i.id,
#                 'question_text': i.question_text
#             }for i in all_question]
#
#         return Response({'test_question': question_list_with_choices},
#                         status=status.HTTP_200_OK)