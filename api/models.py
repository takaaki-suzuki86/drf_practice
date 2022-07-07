from django.db import models


# Create your models here.
class Question(models.Model):
    class Meta:
        app_label = "api"
        managed = False
        db_table = "polls_question"

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
