from rest_framework import serializers
from result.models import UserAnswers
from online_test.serializers import UserSerializer, GetMultipleChoiceSerializer


class GetUserAnswersSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()
    answer = GetMultipleChoiceSerializer()

    class Meta:
        model = UserAnswers
        fields = ('url', 'id', 'user', 'answer')


class PostUserAnswersSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = UserAnswers
        fields = ('url', 'id', 'user', 'answer')