from django.db import models
from django.urls import reverse

#our model for the recipe database
class Recipe(models.Model):
    recipe_title = models.CharField(max_length = 250)
    ingredients = models.TextField()
    instruction = models.TextField()

    #used to retrieve primary key
    def get_absolute_url(self):
        return reverse('cookbook:recipe', kwargs = {'pk': self.pk})

    def __str__(self):
        return self.recipe_title