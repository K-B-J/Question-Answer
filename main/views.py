from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *


def root(request):
    return redirect("main:login")


def login(request):
    if request.method == "GET":
        form = AuthenticationForm()
        return render(request, "login.html", {"form": form})
    else:
        form = AuthenticationForm(request.POST)
        username = request.POST["username"]
        password = request.POST["password"]
        if User.objects.filter(username=username).exists():
            user = User.objects.get(username=username)
            if user.check_password(password):
                user_authenticated = authenticate(
                    request, username=username, password=password
                )
                auth_login(request, user_authenticated)
                return redirect("main:home")
            else:
                return render(
                    request,
                    "login.html",
                    {
                        "form": form,
                        "my_messages": {"error": "Invalid Credentials."},
                    },
                )
        else:
            return render(
                request,
                "login.html",
                {"form": form, "my_messages": {"error": "Invalid Credentials."}},
            )


def register(request):
    if request.method == "GET":
        user_creation_form = UserCreationForm()
        user_info_form = UserInfoForm()
        return render(
            request,
            "register.html",
            {
                "user_info_form": user_info_form,
                "user_creation_form": user_creation_form,
            },
        )
    else:
        user_creation_form = UserCreationForm(request.POST)
        user_info_form = UserInfoForm(request.POST)
        if user_creation_form.is_valid() and user_info_form.is_valid():
            user = user_creation_form.save()
            user_info = user_info_form.save(commit=False)
            user_info.user = user
            user_info.save()
            user_authenticated = authenticate(
                request, username=user.username, password=user.password
            )
            auth_login(request, user_authenticated)
            return redirect("main:home")
        else:
            return render(
                request,
                "register.html",
                {
                    "user_info_form": user_info_form,
                    "user_creation_form": user_creation_form,
                },
            )


@login_required(login_url="main:login")
def logout(request):
    logout(request)
    return redirect("main:login")


@login_required(login_url="main:login")
def home(request):
    return redirect("main:list_questions", 0)


@login_required(login_url="main:login")
def list_questions(request, page_no):
    return render(request, "", {})


@login_required(login_url="main:login")
def ask_question(request):
    if request.method == "GET":
        form = QuestionForm()
        return render(request, "ask_question.html", {"form": form})
    # else:
    #     form = Question(request.)


@login_required(login_url="main:login")
def answer_question(request, question_id):
    pass


@login_required(login_url="main:login")
def view_qa(request, question_id):
    pass


@login_required(login_url="main:login")
def upvote(request, answer_id):
    pass


@login_required(login_url="main:login")
def unupvote(request, answer_id):
    pass
