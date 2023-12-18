from django import template

from mptt_tree_menu.models import MenuItem

register = template.Library()


@register.inclusion_tag('mptt_tree_menu/menu.html', takes_context=True)
def show_menu(context):
    menu_items = MenuItem.objects.filter(level=1)
    return {
        "menu_items": menu_items,
    }

