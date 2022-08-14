from django import template
from django.utils.html import escape
from django.utils.safestring import mark_safe
from django.urls.base import reverse
from django.template.defaultfilters import stringfilter
from django.core.serializers import serialize, deserialize
import re


register = template.Library()

# Inclusion tag displays some data by rendering another template
# @register.inclusion_tag('leaflet/css.html')
# def leaflet_css(plugins=None):  see django-leaflet templatetags

# how to use in template:
# {% load tags_extra %}
# make available one function like:
# {% navactive arg1 arg2 %}

@register.simple_tag
def navactive(request, urls):
    # returns active navigation button
    if request.path in ( reverse(url) for url in urls.split() ):
        return "active"
    return None


readmore_showscript = ''.join([
    "this.parentNode.style.display='none';",
    "this.parentNode.parentNode.getElementsByClassName('more')[0].style.display='inline';",
    "return false;",
]);


@register.simple_tag
def readmore(txt, showwords=15):
    global readmore_showscript
    words = re.split(r' ', escape(txt))

    if len(words) <= showwords:
        return txt

    # wrap the more part
    words.insert(showwords, '<span class="more" style="display:none;">')
    words.append('</span>')

    # insert the readmore part
    words.insert(showwords, '<span class="readmore">... <a href="#" onclick="')
    words.insert(showwords+1, readmore_showscript)
    words.insert(showwords+2, '">read more</a>')
    words.insert(showwords+3, '</span>')

    # Wrap with <p>
    words.insert(0, '<p>')
    words.append('</p>')
    return mark_safe(' '.join(words))

readmore.is_safe = True


# @register.filter
# @stringfilter
# def lower(value):
#     return value.lower()
#
#
@register.simple_tag
def add_str(arg1, arg2):
    """concatenate arg1 & arg2"""
    return str(arg1) + str(arg2)




