from django.shortcuts import render

from .models import Menu
from .utils import logger


def index(request):
    context = {'menus': Menu.objects.all()}
    return render(request, 'menu_app/index.html', context)


def draw_menu(request, path):
    split_path = path.split('/')
    assert len(split_path) > 0, 'Invalid path'
    logger.debug(split_path)
    context = {
        'menu_name': split_path[0],
        'menu_item': split_path[-1]
    }
    return render(
        request, 'menu_app/index.html', context
    )
