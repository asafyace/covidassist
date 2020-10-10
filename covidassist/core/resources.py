from import_export import resources
from .models import Question, Answer, Datasourse


class QuestionResource(resources.ModelResource):
    class Meta:
        model = Question

class AnswerResource(resources.ModelResource):
    class Meta:
        model = Answer


class DatasourseResource(resources.ModelResource):
    class Meta:
        model = Datasourse
