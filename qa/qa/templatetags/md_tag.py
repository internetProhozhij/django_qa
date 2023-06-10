import markdown

#https://docs.djangoproject.com/en/4.2/howto/custom-template-tags/
from django import template
from django.template.defaultfilters import stringfilter


register = template.Library()


@register.filter
@stringfilter
def to_md(text: str) -> str:
    """
    Тег для представления текста в формате .md

    https://learndjango.com/tutorials/django-markdown-tutorial
    """
    return markdown.markdown(text, extensions=["markdown.extensions.fenced_code",
                                               "markdown.extensions.tables"])
    
