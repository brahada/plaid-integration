from django.conf import settings
from django.db import models


class PlaidToken(models.Model):
    access_token = models.CharField(max_length=64, default='')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('access_token', 'user')
