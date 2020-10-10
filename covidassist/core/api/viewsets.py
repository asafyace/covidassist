from rest_framework import viewsets
from core.models import Question, Answer, Datasourse
from .serializers import QuestionSerializer, AnswerSerializer, DatasourseSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class DatasourseViewSet(viewsets.ModelViewSet):
    queryset = Datasourse.objects.all()
    serializer_class = DatasourseSerializer
