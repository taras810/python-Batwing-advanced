from django import template
from main.models import MenuItem

register = template.Library()


@register.inclusion_tag("menu_items_nav.html")
def all_menu_items():
    return {"all_menu_items_list": MenuItem.objects.filter().order_by("-name")}
