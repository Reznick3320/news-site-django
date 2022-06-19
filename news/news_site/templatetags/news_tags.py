from atexit import register
from django import template
from django.db.models import Count, F

from news_site.models import Category

register = template.Library()


@register.simple_tag()
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('news_site/list_categories.html')
def show_categories(val = Category.objects.count):
    # categories = Category.objects.all()
    categories = Category.objects.annotate(cnt=Count('news', filter=F('news__is_pablished'))).filter(cnt__gt=0)
    return {'categories': categories, "val": val}