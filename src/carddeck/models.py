from django.db import models

class CardGroup(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Card(models.Model):
    word = models.CharField(max_length=100)
    group = models.ForeignKey(CardGroup, on_delete=models.CASCADE)
    explanation = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.word}: {self.explanation}"
