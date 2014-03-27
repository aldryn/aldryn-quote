from django.utils.translation import ugettext_lazy as _
from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from aldryn_quote.models import Quote

class QuotePlugin(CMSPluginBase):
    model = Quote
    name = _('Quote')
    render_template = 'aldryn_quote/quote.html'

    def render(self, context, instance, placeholder):
        quote = instance.content
        context.update({
            'quote': quote,
            'footer': instance.footer,
            'url': instance.url,
            'object': instance,
            'placeholder': placeholder
        })
        return context


plugin_pool.register_plugin(QuotePlugin)