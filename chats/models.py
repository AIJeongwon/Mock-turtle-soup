from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=1000)
    question_number = models.IntegerField(default=0)

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=1000)
    answer_number = models.IntegerField(default=0)