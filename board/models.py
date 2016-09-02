# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from users.models import User


@python_2_unicode_compatible
class Post(models.Model):
    """
    Represents an advert of a user on the platform. Its intended to be
    exchangeable for seeds and mainly geolocated oriented (TODOs!)
    """

    date = models.DateTimeField(auto_now_created=True)
    text = models.TextField(max_length=2000)
    date_range = models.DateTimeField()
    # TODO: gps intentional: map = models.¿?
    # TODO: seeds ammount
    # TODO: photomanager album 1-N relationship
    pic = models.ImageField()
    # TODO: https://github.com/zsiciarz/django-pgallery/blob/master/pgallery/models.py#L90
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.username

#    def get_absolute_url(self):
#        return reverse('users:detail', kwargs={'username': self.username})
