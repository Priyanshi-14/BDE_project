from django import template

register = template.Library()

@register.simple_tag(name="zip_lists")
def zip_lists(list1, list2, list3):
    return zip(list1, list2, list3)
