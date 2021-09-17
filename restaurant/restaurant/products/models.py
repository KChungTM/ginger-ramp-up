from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.TextField()
    x = models.IntegerField()
    y = models.IntegerField()
    z = models.IntegerField()
    category = models.TextField()
    rating = models.IntegerField()

    class Meta:
        ordering = ['rating']

    def __str__(self):
        return self.name