# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import status
from rest_framework.request import Request
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.core.urlresolvers import reverse
from rest_framework.test import APIRequestFactory
from online_test.models import Test, Question, MultipleChoice

factory = APIRequestFactory()
request = factory.get('/')
serializer_context = {
    'request': Request(request),
}


class CreateTestTypeTest(APITestCase):

    def setUp(self):
        self.superuser = User.objects.create_superuser(
            'john', 'john@snow.com', 'johnpassword'
        )
        self.client.login(username='john', password='johnpassword')

        self.data = {'name': 'Python',
                     'slug': 'python'}

        def test_can_create_test_type(self):
            response = self.client.post(reverse('test-list'), self.data)
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadTestTypeTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com',
                                                       'johnpassword')
        self.client.login(username='john', password='johnpassword')
        self.test = Test.objects.create(
            name='Python',
            slug='python')

    def test_can_read_test_list(self):
        response = self.client.get(reverse('test-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_read_test_detail(self):
        response = self.client.get(reverse('test-detail',
                                           args=[self.test.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateTestTypeTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com',
                                                       'johnpassword')
        self.client.login(username='john', password='johnpassword')
        self.test = Test.objects.create(
            name='Python',
            slug='python')
        self.data = {'name': 'Python',
                     'slug': 'python'}
        self.data.update({'slug': 'Python'})

    def test_can_update_test(self):
        response = self.client.put(reverse('test-detail',
                                           args=[self.test.id]), self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteTestTypeTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com',
                                                       'johnpassword')
        self.client.login(username='john', password='johnpassword')
        self.test = Test.objects.create(
            name='Python',
            slug='python')

    def test_can_delete_test(self):
        response = self.client.delete(reverse('test-detail',
                                              args=[self.test.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class CreateQuestionTest(APITestCase):

    def setUp(self):
        self.superuser = User.objects.create_superuser(
            'john', 'john@snow.com', 'johnpassword'
        )
        self.client.login(username='john', password='johnpassword')
        self.test = Test.objects.create(name='Python')

        self.data = {'test': reverse('test-detail', args=[self.test.id]),}

        def test_can_create_question(self):
            response = self.client.post(reverse('question-list'), self.data)
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadQuestionTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com',
                                                       'johnpassword')
        self.client.login(username='john', password='johnpassword')
        self.test = Test.objects.create(name='Python')

        self.question = Question.objects.create(test=self.test,
                                                question_text='How are you?')

    def test_can_read_question_list(self):
        response = self.client.get(reverse('question-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_read_question_detail(self):
        response = self.client.get(reverse('question-detail',
                                           args=[self.question.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateQuestionTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com',
                                                       'johnpassword')
        self.client.login(username='john', password='johnpassword')
        self.test = Test.objects.create(name='Python')
        self.question = Question.objects.create(test=self.test,
                                                question_text='How are you?')
        self.data = {''
                     'test': reverse('test-detail', args=[self.test.id]),
                     'question_text': 'How are You?'
                     }
        self.data.update({'question_text': 'Where are you?'})

    def test_can_update_question(self):
        response = self.client.put(reverse('question-detail',
                                           args=[self.question.id]), self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteQuestionTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com',
                                                       'johnpassword')
        self.client.login(username='john', password='johnpassword')
        self.test = Test.objects.create(name='Python')
        self.question = Question.objects.create(test=self.test,
                                                question_text='How are you?')

    def test_can_delete_question(self):
        response = self.client.delete(reverse('question-detail',
                                              args=[self.question.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class CreateMultipleChoiceTest(APITestCase):

    def setUp(self):
        self.superuser = User.objects.create_superuser(
            'john', 'john@snow.com', 'johnpassword'
        )
        self.client.login(username='john', password='johnpassword')
        self.test = Test.objects.create(name='Python')
        self.question = Question.objects.create(test=self.test,
                                                question_text='How are you?')

        self.data = {
            'question': reverse('question-detail', args=[self.question.id]),
            'choice_text': 'good'
        }

        def test_can_create_multiplechoice(self):
            response = self.client.post(reverse('multiplechoice-list'),
                                        self.data)
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadMultipleChoiceTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com',
                                                       'johnpassword')
        self.client.login(username='john', password='johnpassword')
        self.test = Test.objects.create(name='Python')
        self.question = Question.objects.create(test=self.test,
                                                question_text='How are you?')
        self.multiplechoice = MultipleChoice.objects.create(
            question=self.question, choice_text='Cool')

    def test_can_read_multiplechoice_list(self):
        response = self.client.get(reverse('multiplechoice-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_read_multiplechoice_detail(self):
        response = self.client.get(reverse('multiplechoice-detail',
                                           args=[self.multiplechoice.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateMultipleChoiceTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com',
                                                       'johnpassword')
        self.client.login(username='john', password='johnpassword')
        self.test = Test.objects.create(name='Python')
        self.question = Question.objects.create(test=self.test,
                                                question_text='How are you?')
        self.multiplechoice = MultipleChoice.objects.create(
            question=self.question, choice_text='Good')
        self.data = {''
                     'question': reverse('question-detail',
                                         args=[self.question.id]),
                     'choice_text': 'Good'
                     }
        self.data.update({'choice_text': 'Not Cool'})

    def test_can_update_multiplechoice(self):
        response = self.client.put(reverse('multiplechoice-detail',
                                           args=[self.multiplechoice.id]),
                                   self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteMultipleChoiceTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('john', 'john@snow.com',
                                                       'johnpassword')
        self.client.login(username='john', password='johnpassword')
        self.test = Test.objects.create(name='Python')
        self.question = Question.objects.create(test=self.test,
                                                question_text='How are you?')

        self.multiplechoice = MultipleChoice.objects.create(
            question=self.question, choice_text='Cool')

    def test_can_delete_multiplechoice(self):
        response = self.client.delete(reverse('multiplechoice-detail',
                                              args=[self.multiplechoice.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
