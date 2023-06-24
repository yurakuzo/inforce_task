from django.contrib import admin
from .models import Menu, Restaurant


class MenusInline(admin.TabularInline):
    model = Restaurant.menus.through


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['title', 'day', 'price']


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['title',]

    inlines = [
        MenusInline,
    ]