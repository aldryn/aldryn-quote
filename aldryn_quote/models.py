from django.db import models
from django.utils.translation import ugettext_lazy as _
from cms.models import CMSPlugin

# Create your models here.

class Quote(CMSPlugin):
    """
    A quote or testimonial
    """
    content = models.CharField(_('quote'), max_length=255, default='')
    footer = models.CharField(_('footer'), max_length=255, blank=True)
    url = models.URLField(_('url'), blank=True)

    def __unicode__(self):
        return self.content[:50]
