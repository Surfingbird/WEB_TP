from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.paginator import Paginator
# Create your models here.


def get_paginator(questions_list, count):
    return Paginator(questions_list, count)


class QuestionsManager(models.Manager):

    count = 3

    def get_new_questions(self, page_number):
        questions_list = Question.objects.order_by('-question_creation')
        paginator = get_paginator(questions_list, self.count)
        result = paginator.get_page(page_number)
        return result

    def get_hot_questions(self, page_number):
        questions_list = Question.objects.order_by('-question_like__count')
        paginator = get_paginator(questions_list, self.count)
        result = paginator.get_page(page_number)
        return result

    def get_questions_with_tag(self, name_of_tag, page_number):
        tag = Tag.objects.get(tag_name = name_of_tag)
        questions_list = tag.question_id.all()
        paginator = get_paginator(questions_list, self.count)
        result = paginator.get_page(page_number)
        return result


class User(AbstractUser):
    upload = models.ImageField(default=None)

    def __str__(self):
        return str(self.username)

class Question(models.Model):
    question_id = models.IntegerField(
        primary_key=True,
        db_index=True)
    asker_id = models.ForeignKey(User,
                                 on_delete=models.CASCADE,
                                 related_name="questiom_authtor")
    title = models.CharField(max_length=30)
    text = models.TextField(max_length=300)
    is_active = models.BooleanField(default=True)
    have_right_answer = models.BooleanField(default=False)
    question_creation = models.DateTimeField(default=datetime.now())

    objects = QuestionsManager()

    def __str__(self):
        return str(self.question_id)



class Answer(models.Model):
    answer_id = models.IntegerField(
        primary_key=True,
        db_index=True)
    authtor_id = models.ForeignKey(User,
                                   on_delete=models.CASCADE,
                                   related_name="answer_authtor")
    question_id = models.ForeignKey(Question,
                                    on_delete=models.CASCADE,
                                    related_name="answers")
    text = models.TextField(max_length=300)
    is_correct = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    answer_creation = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return str(self.question_id)


class Tag(models.Model):
    tag_name = models.CharField(max_length=10,
                                unique=True,
                                verbose_name='tag_name')
    question_id = models.ManyToManyField(Question,
                                         related_name='Tags')

    def __str__(self):
        return str(self.tag_name)

class Like(models.Model):
    count = models.IntegerField(default=0)

class LikeForQuestion(Like):
    question_id = models.OneToOneField(Question,
                                    on_delete=models.CASCADE,
                                    related_name="question_like")

    def __str__(self):
        return 'question_id ' + str(self.question_id)

class LikeForAnswer(Like):
    answer_id = models.OneToOneField(Answer,
                                  on_delete=models.CASCADE,
                                  related_name="answer_like")

    def __str__(self):
        return 'question_id ' + str(self.answer_id)