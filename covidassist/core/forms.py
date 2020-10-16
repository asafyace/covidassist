from django.forms import ModelForm
from .models import Question


class questionform(ModelForm):
    class Meta:
        model = Question
        fields = ['question']
