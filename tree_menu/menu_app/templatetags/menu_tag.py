from django import template
from django.core.exceptions import ObjectDoesNotExist

from menu_app.models import MenuItem

register = template.Library()


def get_menu(items, menu_item: str = None, submenu: list = None):
    menu = (
        list(items.filter(parent=None))
        if menu_item is None
        else list(items.filter(parent__name=menu_item))
    )
    try:
        menu.insert(menu.index(submenu[0].parent) + 1, submenu)
    except (IndexError, TypeError):
        pass
    try:
        return get_menu(items, items.get(name=menu_item).parent.name, menu)
    except AttributeError:
        return get_menu(items=items, submenu=menu)
    except ObjectDoesNotExist:
        return menu


@register.inclusion_tag("menu_app/menu.html")
def draw_menu(menu_name: str = None, menu_item: str = None):
    items = MenuItem.objects.filter(menu__name=menu_name)
    return (
        {"menu": get_menu(items)}
        if menu_name == menu_item
        else {"menu": get_menu(items, menu_item)}
    )
