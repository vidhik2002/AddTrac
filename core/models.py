from django.db import models


class Word(models.Model):
    input_word = models.CharField(max_length=100)

    def __str__(self):
        return self.input_word