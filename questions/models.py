from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


# Create your models here.
class Question(models.Model):
    asker = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default = timezone.now)
    question = models.CharField(max_length=100)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.question

    def get_absolute_url(self):
        return reverse("question_detail", kwargs={"pk": self.pk})
    


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answer')
    name = models.CharField(max_length=30)
    answer = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f'{self.question} answer from {self.name}'

