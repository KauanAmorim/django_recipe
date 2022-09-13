from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recipes', views.recipes, name='recipes'), # aqui ele deleta essa linha para colocar a linha de baixo, mas e se não retirar?
    path('<int:id>', views.recipe, name='recipe')
]