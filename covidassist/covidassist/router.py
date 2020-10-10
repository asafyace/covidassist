from core.api.viewsets import QuestionViewSet, AnswerViewSet, DatasourseViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('Question', QuestionViewSet)
router.register('Answer', AnswerViewSet)
router.register('Datasource', DatasourseViewSet)
