from rest_framework import serializers
from django.contrib.auth.models import User
from online_test.models import Test, Question, MultipleChoice


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'email', 'first_name', 'last_name',
                  'is_staff', 'is_active', 'is_superuser', 'date_joined',
                  'groups')


class TestSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Test
        fields = ('url', 'id', 'name', 'slug', 'duration', 'no_of_question')


class GetQuestionSerializer(serializers.HyperlinkedModelSerializer):

    test = TestSerializer()
    choices = serializers.SerializerMethodField('choice_list')

    def choice_list(self, test):
        all_choices = MultipleChoice.objects.filter(question__id=test.id)
        choices = [{
            'choice_id': i.id,
            'choice_text': i.choice_text
        }for i in all_choices]
        return choices

    class Meta:
        model = Question
        fields = ('url', 'id', 'question_text', 'test', 'choices')


class PostQuestionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Question
        fields = ('url', 'id', 'question_text', 'test')


class GetMultipleChoiceSerializer(serializers.HyperlinkedModelSerializer):

    question = GetQuestionSerializer()

    class Meta:
        model = MultipleChoice
        fields = ('question', 'url', 'id', 'choice_text', 'is_valid')


class PostMultipleChoiceSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = MultipleChoice
        fields = ('url', 'id', 'choice_text', 'is_valid', 'question')
