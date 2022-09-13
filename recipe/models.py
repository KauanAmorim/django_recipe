from django.db import models
from datetime import datetime

class Recipe(models.model):
    recipe_name = models.CharField(max_length=200)
    ingredients = models.TextField()
    how_to_make = models.TextField()
    time_to_prepare = models.IntegerField()
    qtd_yield = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    date_recipe = models.DateTimeField(default=datetime.now, black=True)

# 1. depois será necessário usar os comandos 
# - python3 manage.py makemigration
# - python3 manage.py migrate
