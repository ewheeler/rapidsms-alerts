from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils.dateformat import format as format_date

NOTIF_STATUS = (
    ('new', 'new'),
    ('fu', 'following up'),
    ('esc', 'escalated'),
    ('closed', 'resolved'),
)

class Notification(models.Model):
    uid = models.CharField(max_length=256)
    created_on = models.DateTimeField(auto_now_add=True)

    text = models.TextField()
    url = models.TextField(null=True, blank=True)

    # link to an AlertType?
    owner = models.ForeignKey(User, null=True, blank=True)
    status = models.CharField(max_length=10, choices=NOTIF_STATUS, default='new')

    def json(self):
        return {
            'id': self.id,
            'msg': self.text,
            'url': self.url,
            'owner': user_name(self.owner),
            'status': self.status,
            'comments': [cmt.json() for cmt in self.comments.all()],
        }

    def __unicode__(self):
        return unicode(self.__dict__)

class NotificationComment(models.Model):
    notification = models.ForeignKey(Notification, related_name='comments')
    user = models.ForeignKey(User, null=True, blank=True) #no user is for system-generated entries
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    def json(self):
        return {
            'text': self.text,
            'date_fmt': format_date(self.date, 'M j, H:i'),
            'author': user_name(self.user, default=settings.SYSTEM_USERNAME),
            'is_system': self.user is None,
        }

    def __unicode__(self):
        return unicode(self.__dict__)

def user_name(user, default=None):
    if user is None:
        return default
    else:
        fname = user.first_name
        lname = user.last_name
        return '%s %s' % (fname, lname) if fname and lname else user.username

class ResolutionAcknowledgement:
    pass