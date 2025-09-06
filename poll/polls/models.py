from django.db import models

# Create your models here.


class question(models.Model):
    question_text = models.TextField(max_length=200)
    pub_date = models.DateTimeField("date published")

class Choices(models.Model):
    question = models.ForeignKey(question, on_delete=models.CASCADE)
    Choices_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              