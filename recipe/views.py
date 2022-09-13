from django.shortcuts import get_object_or_404, render
from recipe.models import Recipe # ou .models

def index(request):
    # recipes = {
    #     1: 'Lasanha',
    #     2: 'Sopa de legumes',
    #     3: 'Sorvete',
    #     4: 'Bolo de chocolate'
    # }

    recipes = Recipe.objects.all()
    data = { 'recipes': recipes }
    return render(request, 'index.html', data)

def recipes(request):
    return render(request, 'recipe.html')

def recipe(request, id):

    recipe = get_object_or_404(Recipe, pk=id)
    data = { 'recipe': recipe }
    return render(request, 'recipe.html', data)


# 3. executar comando depois depois
# - pip install pylint-django

# adicionar isso em settings.json
# {
#     "python.pythonPath": "venv/bin/python",
#     "python.linting.pylintArgs": [
#         "--load-plugins=pylint_django"
#     ],
# }
