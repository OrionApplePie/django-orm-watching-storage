from datetime import datetime, timezone, timedelta
from django.db import models


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def get_duration(self):
        if not self.leaved_at:
            return datetime.now(timezone.utc) - self.entered_at
        return self.leaved_at - self.entered_at

    def is_visit_long(self, minutes=60):
        return self.get_duration() > timedelta(minutes=minutes)

    @staticmethod
    def format_duration(duration):
        seconds = duration.seconds
        hours = seconds // 3600
        minutes = (seconds // 60) % 60
        return f'{hours}ч {minutes}мин'

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved= 'leaved at ' + str(self.leaved_at) if self.leaved_at else 'not leaved'
        )
