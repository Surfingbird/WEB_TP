from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.http import Http404

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.

def index(request, page_number = 1):
    contact_list = [1, 6, 7, 10, 33, 48, 10, 9, 8, 7, 4, 3];
    paginator = Paginator(contact_list, 3)

    template = loader.get_template('questions/index.html')
    contacts = paginator.get_page(page_number)
    return HttpResponse(template.render(context={'questions' : contacts}))


# def index(request, page_number = 1):
#     likes = [1, 6, 7, 10, 33, 48];
#     data = {'questions' : likes}
#     template = loader.get_template('questions/index.html')
#     return HttpResponse(template.render(context=data))

def hot(request, page_number = 1):
    likes = [10, 9, 8, 7, 4, 3];
    data = {'questions': likes}
    template = loader.get_template('questions/index.html')
    return HttpResponse(template.render(context=data))

def tag(request, tag_name):
    # template = loader.get_template('questions/base.html')
    return HttpResponse('tag' + str(tag_name))

def question(request, question_id):
    # template = loader.get_template('questions/base.html')
    return HttpResponse('question' + str(question_id))

def login(request):
    template = loader.get_template('questions/login.html')
    return HttpResponse(template.render())

def signup(request):
    template = loader.get_template('questions/signup.html')
    return HttpResponse(template.render())

def ask(request):
    template = loader.get_template('questions/ask.html')
    return HttpResponse(template.render())

def test(request):
    header = "Personal Data"  # обычная переменная
    langs = ["English", "German", "Spanish"]  # массив
    user = {"name": "Tom", "age": 23}  # словарь
    addr = ("Абрикосовая", 23, 45)  # кортеж

    data = {"header": header, "langs": langs, "user": user, "address": addr}

    return HttpResponse(render(request, "questions/test.html", context=data))