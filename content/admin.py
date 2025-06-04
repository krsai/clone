from django.contrib import admin
from .models import Material, Movement

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('name', 'stock')

@admin.register(Movement)
class MovementAdmin(admin.ModelAdmin):
    list_display = ('material', 'movement_type', 'quantity', 'timestamp')
    list_filter = ('movement_type', 'timestamp')
