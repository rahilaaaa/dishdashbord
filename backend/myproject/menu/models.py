from django.db import models

class Dish(models.Model):
    dishId = models.CharField(max_length=10, primary_key=True)
    dishName = models.CharField(max_length=100)
    imageUrl = models.URLField()
    isPublished = models.BooleanField(default=False)
