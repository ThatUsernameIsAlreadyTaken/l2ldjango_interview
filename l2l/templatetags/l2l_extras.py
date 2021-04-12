from django import template
from datetime import datetime

register = template.Library()


@register.filter(name='l2l_dt')
def l2l_dt(value):
    str_value = str(value)
    st = str_value.split(".")
    print(st)
    try:
        st = st[0].split("T")
        st = st[0] + " " + st[1]
        new = datetime.strptime(st, "%Y-%m-%d %H:%M:%S")
    except Exception as e:
        print(e)
        new = datetime.strptime(st[0], "%Y-%m-%d %H:%M:%S")
    return new

