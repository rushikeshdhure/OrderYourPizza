from django.contrib import admin

from .models import AddPizza

@admin.register(AddPizza)
class PizzaAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'is_available', 'created_at']
    list_filter = ['is_available', 'created_at']
    search_fields = ['name', 'description']