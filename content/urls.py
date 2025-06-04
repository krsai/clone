from django.urls import path
from .views import (
    MaterialListView, MaterialCreateView,
    MovementListView, MovementCreateView
)

urlpatterns = [
    path('materials/', MaterialListView.as_view(), name='material_list'),
    path('materials/add/', MaterialCreateView.as_view(), name='material_add'),
    path('movements/', MovementListView.as_view(), name='movement_list'),
    path('movements/add/', MovementCreateView.as_view(), name='movement_add'),
]
