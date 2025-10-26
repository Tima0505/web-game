from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=255)
    answer_text = models.CharField(max_length=255)

    def __str__(self):
        return self.question_text

class Player(models.Model):
    name = models.CharField(max_length=100)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.name

# Create your models here.
