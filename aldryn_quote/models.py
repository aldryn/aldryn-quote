from django.utils.timezone import now
from django.db import models
from django.utils.translation import ugettext_lazy as _
from cms.models import CMSPlugin

# Create your models here.

class Quote(CMSPlugin):
    """
    A quote or testimonial
    """
    created_at = models.DateTimeField(_('Created at'), default=now)
    content = models.CharField(_('Quote'), max_length=255, default='')
    footer = models.CharField(_('Footer'), max_length=255, blank=True)
    url = models.URLField(_('Link'), blank=True)
    target = models.CharField(_('Target'), max_length=50, blank=True, default='_blank', choices=(
        ('_blank',  _("New window")),
    ))

    def __unicode__(self):
        return self.content[:50]
