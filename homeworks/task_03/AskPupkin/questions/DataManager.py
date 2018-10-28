from questions.models import User, Question, Tag, Answer, LikeForAnswer, LikeForQuestion

from faker import Faker
import random

def create_new_users(n):
    f = Faker()
    for i in range(n):
        name = f.name()
        u = User(
            username = f.name(),
            first_name = name.split()[0],
            last_name = name.split()[1],
            email = f.email(),
            password = f.password(),
            is_staff = False,
            is_active = True,
        )
        u.save()
    # date_joined = f.date_time()

def create_for_all_users_questions(n):
    f = Faker()
    for i in User.objects.all():
        for j in range(n):
            q = Question(
                asker_id=i,
                title = f.text(30),
                text = f.text(300)
            )
            q.save()
#
# def create_tags_for_questions():
#     f = Faker()
#     for i in Question.objects.all():
#         for j in range(random.randint(1, 4)):
#             t = Tag(
#                 tag_name = f.word(),
#                 question_id = i
#             )
#             t.save()

def create_answers_for_questions():
    f = Faker()
    for i in Question.objects.all():
        for j in range(random.randint(1, 4)):
            answer = Answer(
                question_id = i,
                authtor_id = User.objects.all()[random.randint(1,User.objects.count() - 1)],
                text = f.text(300),
                is_correct = False
            )
            answer.save()

def create_likes_for_answers():
    f = Faker()
    for i in Answer.objects.all():
        like = LikeForAnswer(
            count = random.randint(0, 10),
            answer_id = i
        )
        like.save()

def create_likes_for_questions():
    f = Faker()
    for i in Question.objects.all():
        like = LikeForQuestion(
            count = random.randint(0, 10),
            question_id = i
        )
        like.save()


def create_tags(n):
    f = Faker()
    for i in range(n):
        tag = Tag(tag_name = f.word())
        tag.save()

def give_n_tags_for_questions():
    for i in range(1, Question.objects.count() + 1):
        # for j in range(random.randint(1, n)):
            q = Question.objects.get(pk = i)
            q.Tags.add(Tag.objects.get(pk = random.randint(1, 10)))
            q.save()
