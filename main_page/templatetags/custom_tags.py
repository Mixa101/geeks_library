from django import template

register = template.Library()

@register.simple_tag
def get_rate(book):
    average_rate = sum([book.comments.all()[i].rate_with_default for i in range(5)]) // 5
    return average_rate