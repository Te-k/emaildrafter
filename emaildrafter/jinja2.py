"""Setup file for Jinja2 templating, mapping Jinja2's functions: static(), url() and url_for() to Django's equivalents"""
from django.templatetags.static import static
from django.urls import reverse

from jinja2 import Environment


def environment(**options):
    env = Environment(**options)
    env.globals.update(
        {"static": static, "url": reverse, "url_for": reverse,}
    )
    return env