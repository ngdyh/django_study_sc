"""authot:
   data:
"""

from django import template
from django.conf import settings

# 注册到template库里面
register = template.Library()

# 自定义Tag
@register.simple_tag
def mystatic(value):
    # STATIC_UTL + value
    return settings.STATIC_URL+value
