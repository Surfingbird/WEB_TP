from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Question(models.Model):
    question_id = models.IntegerField(primary_key=True, db_index=True)
    asker_id = models.ForeignKey( # Many to one
        'ExtraUser',
        on_delete=models.CASCADE
    )
    questions_title = models.CharField(max_length=30)
    questions_text = models.CharField(max_length=300)
    date_of_creation = models.DateTimeField()

class Answer(models.Model):
    answer_id = models.IntegerField(
        primary_key=True,
        db_index=True
    )
    question_id = models.ForeignKey( # Many to one
        Question,
        on_delete=models.CASCADE #удаление null связей
    ) #По умолчанию связывание primary_key
    teller_id = models.OneToOneField(
        'ExtraUser',
        on_delete = models.CASCADE
    )
    answers_title = models.CharField(max_length=30)
    answers_text = models.CharField(max_length=300)
    date_of_creation = models.DateTimeField()

# class Like(models.Model): Нужно ли отнаследовать лайки вопросов и лайки ответов от общей абстракции лайк?
#     question_id = models.IntegerField(primary_key=True)
#     count = models.IntegerField()

class Tag(models.Model):
    pass;

class ExtraUser(User):
    user_id = models.IntegerField(
        primary_key=True,
        db_index=True
    )

class Profil():
    user_id = models.OneToOneField(
        ExtraUser,
        on_delete=models.CASCADE
    )
    avatar = models.ImageField()

class Smth(models.Model):
    id = models.IntegerField(
        primary_key=True,
        db_index=True
    )
    string = models.CharField(max_length=30)


# class UsersProfil(models.Model): #его надо отнаследовать !
#     user_id = models.IntegerField(primary_key=True, unique=True, db_index=True)
#     nikename = models.CharField(max_length=30)
#     #mail_address
#     raitind = models.IntegerField()