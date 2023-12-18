from django.shortcuts import render

from .models import Menu


def index(request):
    return render(
        request, 'menu_app/index.html', {'menus': Menu.objects.all()}
    )


def draw_menu(request, path):
    splitted_path = path.split('/')
    return render(
        request,
        'menu_app/index.html',
        {'menu_name': splitted_path[0], 'menu_item': splitted_path[-1]}
    )