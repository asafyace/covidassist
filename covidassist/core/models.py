from django.db import models
from django.conf import settings


class Question(models.Model):
    question = models.CharField(max_length=120, null=True, blank=True)

    def __str__(self):
        return self.question


class Answer(models.Model):
    answer = models.CharField(max_length=120, null=True, blank=True)

    def __str__(self):
        return self.answer


class Datasourse(models.Model):
    datasourse = models.CharField(max_length=120, null=True, blank=True)

    def __str__(self):
        return self.datasourse
