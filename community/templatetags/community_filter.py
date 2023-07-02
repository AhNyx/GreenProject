from django import template

register = template.Library()


@register.filter
def sub(value, arg):    # -(마이너스)를 sub라는 이름으로 탬플릿태그로 정의
    return value - arg
