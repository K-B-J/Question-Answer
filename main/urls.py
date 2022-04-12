from django.urls import path
from main import views

app_name = "main"

urlpatterns = [
    path("", views.root, name="root"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("register/", views.register, name="register"),
    path("home/", views.home, name="home"),
    path("home/<int:id>", views.list_questions, name="list_questions"),
    path("ask_question/", views.ask_question, name="ask_question"),
    path("answer_question/<int:id>", views.answer_question, name="answer_question"),
    path("upvote/<int:id>", views.upvote, name="upvote"),
    path("unupvote/<int:id>", views.unupvote, name="unupvote"),
]
