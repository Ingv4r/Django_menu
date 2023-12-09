from django.db.models import QuerySet

from tree_menu.menu_app.models import MenuItem
from django import template
from django.core.exceptions import ObjectDoesNotExist


register = template.Library()


def get_menu(
        items: QuerySet,
        menu_item: str = None,
        submenu: list = None
) -> list[list | None]:
    if menu_item is None:
        menu = list(items.filter(parent=None))
    else:
        menu = list(items.filter(parent__name=menu_item))
    try:
        menu.insert(menu.index(submenu[0].parent) + 1, submenu)
    except (IndexError, TypeError):
        pass
    try:
        return get_menu(
            items,
            items.get(name=menu_item).parent.name,
            submenu=menu
        )
    except AttributeError:
        return get_menu(items, submenu=menu)
    except ObjectDoesNotExist:
        return menu


@register.inclusion_tag('menu_app/menu.html')
def dram_menu(menu_name: str = None, menu_item: str = None) -> dict:
    items = MenuItem.objects.filter(menu__name=menu_name)
    if menu_name == menu_item:
        return {'menu': get_menu(items)}
    return {'menu': get_menu(items, menu_item)}
