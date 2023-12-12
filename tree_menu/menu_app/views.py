from django.shortcuts import render
from django.db import connection

from .models import Menu


def index(request):
    context = {"menus": Menu.objects.all()}
    return render(request, "menu_app/index.html", context)


def draw_menu(request, path):
    split_path = path.split("/")
    context = {"menu_name": split_path[0], "menu_item": split_path[-1]}
    return render(request, "menu_app/index.html", context)
