from django.urls import path

from . import views

app_name = 'questions'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:page_number>/', views.index, name='index'),
    path('hot/', views.hot, name='hot'),
    path('hot/<int:page_number>/', views.hot, name='hot'),
    path('tag/<str:tag_name>/', views.tag, name='tag'),
    path('tag/<str:tag_name>/<int:page_number>/', views.tag, name='tag'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('ask/', views.ask, name='ask'),
    path('question/', views.question, name='question'),
    path('question/<int:question_id>/', views.question, name='question'),
    path('test/', views.test, name='test'),
]

