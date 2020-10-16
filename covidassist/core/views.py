from django.views import View
from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from .models import Question, Answer, Datasourse
from .forms import questionform


def home_page(request):
    my_title = "Covid Assist"
    return render(request, "covid_assist.html", {"title": my_title})
