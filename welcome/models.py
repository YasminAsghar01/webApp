from django.db import models
from unittest.util import _MAX_LENGTH
import datetime
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField(default=datetime.date.today)
    image = models.ImageField(default='/images/defaultProfile.jpg', upload_to='images/')
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.username

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'dob': self.dob,
            'email': self.email,
            'image': self.image.url if self.image else None,
            'password': self.password,
        }


class Item(models.Model):
    title = models.CharField(max_length=500, blank=True)
    image = models.ImageField(default='/images/car.jpg', upload_to='images/')
    description = models.CharField(max_length=1000, blank=True)
    startingPrice = models.DecimalField(
        max_digits=11, decimal_places=2, null=True)
    finishDate = models.DateField(null=True)
    owner = models.CharField(max_length=500)

    def to_dict(self):
        """returns the object asigning each attribute"""
        return {
            "id": self.id,
            "title": self.title,
            'image': self.image.url if self.image else None,
            "description": self.description,
            "startingPrice": self.startingPrice,
            "finishDate": self.finishDate,
            "owner": self.owner,
        }


class PageView(models.Model):
    hostname = models.CharField(max_length=32)
    timestamp = models.DateTimeField(auto_now_add=True)


class Question(models.Model):
    question = models.CharField(max_length=80)
    user = models.CharField(max_length=32)
    item = models.CharField(max_length=32)

    def __str__(self):
        return self.question

    def to_dict(self):
        return {
            'id': self.id,
            'item': self.item,
            'question': self.question
        }


class Answer(models.Model):
    question = models.OneToOneField(
        Question,
        on_delete=models.CASCADE,
    )
    answer = models.CharField(max_length=80)
    user = models.CharField(max_length=32)
    item = models.CharField(max_length=32)

    def __str__(self):
        return self.answer

    def to_dict(self):
        return {
            'question': self.question.question,
            'user': self.user,
            'answer': self.answer,
            'item': self.item
        }

    class Meta:
        ordering = ['question']
