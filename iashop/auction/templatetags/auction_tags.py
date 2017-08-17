import datetime, time
from django import template

register = template.Library()

@register.filter(name='to_json')
def to_json(t):
    if isinstance(t, datetime.datetime):
        return '{}'.format(int(time.mktime(t.timetuple()))*1000)
    else:
        return 'Wrong format'

