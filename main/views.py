from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.http import HttpResponseNotFound


def root(request):
    return redirect("main:login")


def login(request):
    if request.method == "GET":
        form = AuthenticationForm()
        if "my_messages" in request.session:
            my_messages = request.session["my_messages"]
            del request.session["my_messages"]
            return render(
                request, "login.html", {"form": form, "my_messages": my_messages}
            )
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
                        "my_messages": {
                            "error": True,
                            "message": "Invalid Credentials",
                        },
                    },
                )
        else:
            return render(
                request,
                "login.html",
                {
                    "form": form,
                    "my_messages": {"error": True, "message": "Invalid Credentials"},
                },
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
            request.session["my_messages"] = {
                "success": True,
                "message": "Registration Successful",
            }
            return redirect("main:login")
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
    auth_logout(request)
    request.session["my_messages"] = {
        "success": True,
        "message": "Logged Out Successfully",
    }
    return redirect("main:login")


@login_required(login_url="main:login")
def home(request):
    return redirect("main:list_questions", 0)


@login_required(login_url="main:login")
def list_questions(request, page_no):
    if page_no == 0:
        questions_data = Question.objects.all()
        questions = []
        for question in questions_data:
            if not Answer.objects.filter(question=question).exists():
                questions.append({"id": question.id, "question": question.question})
        context = {"questions": questions[::-1]}
        if "my_messages" in request.session:
            context["my_messages"] = request.session["my_messages"]
            del request.session["my_messages"]
        return render(request, "home0.html", context)
    elif page_no == 1:
        questions_data = Question.objects.all()
        questions = []
        for question in questions_data:
            if Answer.objects.filter(question=question).exists():
                questions.append({"id": question.id, "question": question.question})
        context = {"questions": questions[::-1]}
        if "my_messages" in request.session:
            context["my_messages"] = request.session["my_messages"]
            del request.session["my_messages"]
        return render(request, "home1.html", context)
    else:
        return HttpResponseNotFound()


@login_required(login_url="main:login")
def ask_question(request):
    if request.method == "GET":
        form = QuestionForm()
        return render(request, "ask_question.html", {"form": form})
    else:
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = UserInfo.objects.get(user=request.user)
            question.save()
            request.session["my_messages"] = {
                "success": True,
                "message": "Question Posted Successfully",
            }
            return redirect("main:home")
        else:
            return render(request, "ask_question.html", {"form": form})


@login_required(login_url="main:login")
def answer_question(request, question_id):
    if request.method == "GET":
        form = AnswerForm()
        question = "asdfasdf"  # write logic to fetch question here
        return render(
            request, "answer_question.html", {"form": form, "question": question}
        )
    # else:
    # submit answer logic with message


@login_required(login_url="main:login")
def view_qa(request, question_id):
    if Question.objects.filter(id=question_id).exists():
        question = Question.objects.get(id=question_id)
        answers = []
        for answer in Answer.objects.filter(question=question):
            votes = str(AnswerUpvote.objects.filter(answer=answer).count())
            voted = AnswerUpvote.objects.filter(
                user=UserInfo.objects.get(user=request.user)
            ).exists()
            answers.append(
                {
                    "votes": votes,
                    "answer": answer.answer,
                    "answer_id": answer.id,
                    "voted": voted,
                }
            )
        answers = sorted(answers, key=lambda d: d["votes"])
        context = {
            "question": question.question,
            "question_id": question_id,
            "answers": answers,
        }
        if "my_messages" in request.session:
            context["my_messages"] = request.session["my_messages"]
            del request.session["my_messages"]
        return render(
            request,
            "view_qa.html",
            context,
        )
    else:
        return HttpResponseNotFound()


# complete the whole upvote and unupvote logic and working
@login_required(login_url="main:login")
def upvote(request, answer_id):
    pass


@login_required(login_url="main:login")
def unupvote(request, answer_id):
    pass
