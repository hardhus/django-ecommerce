from django import template


register = template.Library()

@register.inclusion_tag("main/templatetags/circle_item.html", takes_context=True)
def circle_header_item(context):
    return context