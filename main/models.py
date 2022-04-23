from django.db import models
from django.contrib.auth.models import User


class UserInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    email = models.EmailField()
    mobile_no = models.CharField(max_length=20)
    dob = models.DateField()

    def __str__(self) -> str:
        return self.first_name


class Question(models.Model):
    user = models.ForeignKey(UserInfo, on_delete=models.DO_NOTHING)
    question = models.TextField()

    def __str__(self) -> str:
        return self.question


class Answer(models.Model):
    user = models.ForeignKey(UserInfo, on_delete=models.DO_NOTHING)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.TextField()

    def __str__(self) -> str:
        return self.answer


class AnswerUpvote(models.Model):
    question = models.ForeignKey(Answer, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
