from rest_framework import serializers
from core.models import Question, Answer, Datasourse


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = (
            'id',
            'question',
        )
        read_only_fields = ['id']


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = (
            'id',
            'answer',
        )
        read_only_fields = ['id']


class DatasourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Datasourse
        fields = (
            'id',
            'datasourse',
        )
        read_only_fields = ['id']
