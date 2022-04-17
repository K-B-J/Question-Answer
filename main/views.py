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
            # instead of login show message and ask to login
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
    auth_logout(request)
    # show message of logout successfull
    return redirect("main:login")


@login_required(login_url="main:login")
def home(request):
    return redirect("main:list_questions", 0)


@login_required(login_url="main:login")
def list_questions(request, page_no):
    if page_no == 0:
        questions = [
            {"id": 1, "question": "How is a bubble sort algorithm implemented?"},
            {
                "id": 2,
                "question": "How to print the first non-repeated character from a string?",
            },
            {
                "id": 3,
                "question": "How to find the first non repeated character of a given String?",
            },
            {
                "id": 4,
                "question": "How do you find duplicate numbers in an array if it contains multiple duplicates?",
            },
            {
                "id": 5,
                "question": "How do you remove duplicates from an array in place?",
            },
            {
                "id": 6,
                "question": "How are duplicates removed from an array without using any library?",
            },
            {
                "id": 7,
                "question": "How do you find the middle element of a singly linked list in one pass?",
            },
            {
                "id": 8,
                "question": "How do you check if a given linked list contains a cycle? How will you find initial node of the cycle?",
            },
            {
                "id": 5,
                "question": "How do you remove duplicates from an array in place?",
            },
            {
                "id": 6,
                "question": "How are duplicates removed from an array without using any library?",
            },
            {
                "id": 7,
                "question": "How do you find the middle element of a singly linked list in one pass?",
            },
        ]  # logic to fetch questions
        return render(request, "home0.html", {"questions": questions})
    elif page_no == 1:
        questions = [
            {"id": 3, "question": "3"},
            {"id": 4, "question": "4"},
        ]  # logic to fetch questions
        return render(request, "home1.html", {"questions": questions})
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
            form.save()
            # Add logic to show message that question is posted
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
    # logic to see if question id is correct
    question = "How do you find the middle element of a singly linked list in one pass?"  # fetch the question here
    answers = [
        {
            "votes": "24",
            "answer": "Traverse the whole linked list and count the no. of nodes. Now traverse the list again till count/2 and return the node at count/2.",
            "voted": True,
        },
        {
            "votes": "12",
            "answer": "Traverse linked list using two pointers. Move one pointer by one and the other pointers by two. When the fast pointer reaches the end slow pointer will reach the middle of the linked list.",
            "voted": False,
        },
    ]  # fetch answers
    # write the logic to sort and format the votes
    return render(
        request,
        "view_qa.html",
        {"question": question, "question_id": question_id, "answers": answers},
    )


# complete the whole upvote and unupvote logic and working
@login_required(login_url="main:login")
def upvote(request, answer_id):
    pass


@login_required(login_url="main:login")
def unupvote(request, answer_id):
    pass
