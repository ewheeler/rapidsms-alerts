import json
import itertools

from django import template
from django.template import RequestContext
from django.template.loader import render_to_string

from alerts.models import Notification
from alerts.utils import get_alert_generators

register = template.Library()

@register.inclusion_tag("alerts/partials/alerts.html", takes_context=True)
def alerts(context):
    request = context['request']
    alerts = itertools.chain(*(g for g in get_alert_generators('alert', request=request, context=context) if g is not None))
    return {"alerts": alerts}

@register.simple_tag(takes_context=True)
def notifications(context):
    request = context['request']
    if request.user.is_authenticated():
        notifs = Notification.objects.filter(is_open=True, visible_to__user=request.user)
        data = json.dumps([notif.json(request.user) for notif in notifs])

        return render_to_string("alerts/partials/notifications.html",
                                {"notifs": notifs,
                                "notif_data": data}, context_instance=RequestContext(request))
    return ""

