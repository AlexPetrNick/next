from django.contrib.auth.models import User
from django.db import models

TomateChoise = (
    ("b", "BAD"),
    ("g", "GOOD"),
    ("n", "NORMAL"),
)


class UserModel(models.Model):
    first_name = models.CharField(max_length=15)
    second_name = models.CharField(max_length=15)
    verify_user = models.BooleanField(default=False)
    movies = models.ManyToManyField("Movie")

    def __str__(self):
        return f"{self.first_name} {self.second_name}"


class FeedBack(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey("Movie", on_delete=models.CASCADE)
    feedback = models.CharField(max_length=400)


class Movie(models.Model):
    title = models.CharField(max_length=20)
    tomate_rating = models.CharField(TomateChoise,
                                     choices=TomateChoise,
                                     default=TomateChoise[0],
                                     max_length=6)
    # feedback_id = models.ManyToOneRel("FeedBack", "feedback_id", "id")

    def __str__(self):
        return self.title


class StatusCode(models.Model):
    code = models.CharField(unique=True, max_length=20)
    description = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.code} - {self.description}"
