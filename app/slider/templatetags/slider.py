from django import template
from ..models import Slider


register = template.Library()


@register.inclusion_tag('site/tags/slides.html')
def slider():
    items = Slider.objects.all()
    return{'items':items}
