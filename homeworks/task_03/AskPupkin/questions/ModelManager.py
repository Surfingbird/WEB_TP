from django.core.paginator import Paginator
from .models import *


def get_paginator(questions_list, count):
    return Paginator(questions_list, count)

class ModelManager():

    count = 3

    def get_new_questions(self, page_number):
        questions_list = Question.objects.order_by('-question_creation')
        paginator = get_paginator(questions_list, count)
        result = paginator.get_page(page_number)
        return result

    def get_hot_questions(self, page_number):
        questions_list = Question.objects.order_by('-question_like__count')
        paginator = get_paginator(questions_list, count)
        result = paginator.get_page(page_number)
        return result

    def get_questions_with_tag(self, tag_name):
        pass







