from django.db import models


# Create your models here.

class Quizz(models.Model):
    categorie = models.CharField(max_length=25)
    title = models.CharField(max_length=150)
    niveau = models.CharField(max_length=50)
    nbr_px = models.IntegerField()


class Proposition(models.Model):
    proposition = models.TextField()


class Question(models.Model):
    categorie = models.ForeignKey(Quizz, on_delete=models.PROTECT)
    question = models.TextField()
    proposition = models.ForeignKey(Proposition, on_delete=models.CASCADE)
    nbr_points = models.IntegerField()
