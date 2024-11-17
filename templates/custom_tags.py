from django import template

register = template.Library()

@register.simple_tag
def get_rate(book):
    average_rate = sum([i for i in book.comments.all()])
    return average_rate