from django.contrib import admin
from recipe.models import Recipe

admin.site.register(Recipe)

# 2. depois disso será necessário usar o comando
# - python3 manage.py createsuperuser
# mas como é para testes, não precisa de um usuário normal.

