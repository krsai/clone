from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Material, Movement
from .forms import MaterialForm, MovementForm

class MaterialListView(ListView):
    model = Material
    template_name = 'content/material_list.html'
    context_object_name = 'materials'

class MaterialCreateView(CreateView):
    model = Material
    form_class = MaterialForm
    template_name = 'content/material_form.html'
    success_url = reverse_lazy('material_list')

class MovementListView(ListView):
    model = Movement
    template_name = 'content/movement_list.html'
    context_object_name = 'movements'

class MovementCreateView(CreateView):
    model = Movement
    form_class = MovementForm
    template_name = 'content/movement_form.html'
    success_url = reverse_lazy('movement_list')
