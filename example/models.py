from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField("Title", max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title