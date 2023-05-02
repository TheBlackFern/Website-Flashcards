from django.db import models

class CardGroup(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Card(models.Model):
    word = models.CharField(max_length=100)
    group = models.ForeignKey(CardGroup, on_delete=models.CASCADE)
    explanation = models.CharField(max_length=100)
    level = models.IntegerField(default=0)

    def get_color_palette(self):
        if 2 < self.level <= 4:
            return "bg-white dark:bg-gray-800 border-amber-300 dark:border-amber-700"
        if 4 < self.level <= 8:
            return "bg-white dark:bg-gray-800 border-blue-500 dark:border-teal-600 shadow-mid"
        if 8 < self.level:
            return "bg-white dark:bg-gray-800 border-fuchsia-600 dark:border-fuchsia-800 shadow-top"
        return "bg-white dark:bg-gray-800 border-gray-200 dark:border-gray-700"

    def __str__(self):
        return f"{self.word}: {self.explanation}"
