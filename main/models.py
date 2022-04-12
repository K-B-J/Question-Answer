from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    question = models.TextField()

    def __str__(self) -> str:
        return self.question


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.TextField()

    def __str__(self) -> str:
        return self.answer


class AnswerUpvote(models.Model):
    question = models.ForeignKey(Answer, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
