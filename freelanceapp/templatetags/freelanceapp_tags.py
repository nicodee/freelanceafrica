from django import template
from urllib import urlencode
from urllib2 import urlopen
from django.db.models import Q

register = template.Library()

# @register.filter(name='get_due_date_string')
# def get_due_date_string(value):
#     pass

# @register.filter(name='nick')
# def nick(value):
#     return "nick"

# @register.filter(name='get_google_analytics')
# def get_google_analytics(value):
#     pass

# @register.inclusion_tag('google_analytics.html')
# def google_analytics():
#     pass

@register.inclusion_tag('account_settings_nav.html')
def account_settings_nav():
    pass

# @register.inclusion_tag('footer.html')
# def footer():
#     pass

# @register.inclusion_tag('endless_figure_js.html')
# def endless_figure_js():
#     pass




