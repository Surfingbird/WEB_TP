from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.http import Http404
from .models import *
from .ModelManager import *

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.

def get_paginator(contact_list, count):
    return Paginator(contact_list, count)

def index(request, page_number = 1): #full
    template = loader.get_template('questions/index.html')
    try:
        questions_on_page = Question.objects.get_new_questions(page_number)
    except:
        raise Http404("We have not this question(((")
    return HttpResponse(template.render(context={'questions_on_page' : questions_on_page,
                                                 'proxy_to': 'questions:index'}))

def hot(request, page_number = 1):  # full
    template = loader.get_template('questions/index.html')
    try:
        questions_on_page = Question.objects.get_hot_questions(page_number)
    except:
        raise Http404("We have not this question(((")
    return HttpResponse(template.render(context={'questions_on_page' : questions_on_page,
                                                 'proxy_to': 'questions:hot'}))

def tag(request, tag_name, page_number = 1): # нормально не работает
    template = loader.get_template('questions/index.html')
    try:
        questions_on_page = Question.objects.get_questions_with_tag(tag_name, page_number)
    except:
        raise Http404("We have not this tag(((")
    return HttpResponse(template.render(context={'questions_on_page': questions_on_page,
                                                 'proxy_to': 'questions:tag',
                                                 'arg' : tag_name}))

def question(request, question_id = 1): #full
    template = loader.get_template('questions/question.html')
    try:
        question = Question.objects.get(pk = question_id)
        context = {'question' : question}
    except:
        raise Http404("We have not this question(((")

    return HttpResponse(template.render(context))

def login(request): #full
    template = loader.get_template('questions/login.html')
    return HttpResponse(template.render())

def signup(request): #full
    template = loader.get_template('questions/signup.html')
    return HttpResponse(template.render())

def ask(request): #full
    template = loader.get_template('questions/ask.html')
    return HttpResponse(template.render())

def test(request):
    template = loader.get_template('questions/test.html')
    # rell = "{% url 'questions:index' %}"
    rell = 'questions:hot'
    return HttpResponse(template.render(context={'rell' : rell, 'proxy_to' : 'questions:index'}))

