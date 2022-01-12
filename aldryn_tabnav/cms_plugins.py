from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .conf import settings
from .models import TabGroupPlugin, TabPlugin, TabDropDownPlugin


class CMSTabGroupPlugin(CMSPluginBase):
    model = TabGroupPlugin
    name = _('Tab Group')
    module = _('Tabs')
    allow_children = True
    child_classes = ['CMSDropdownTabPlugin', 'CMSTabPlugin']
    render_template = settings.ALDRYN_TABNAV_DEFAULT_TEMPLATE

    def render(self, context, instance, placeholder):
        self.render_template = instance.layout_template
        return super(CMSTabGroupPlugin, self).render(context, instance, placeholder)


class CMSTabPlugin(CMSPluginBase):
    model = TabPlugin
    name = _('Tab')
    module = _('Tabs')
    render_template = "aldryn_tabnav/tab.html"
    allow_children = True
    parent_classes = ['CMSDropdownTabPlugin', 'CMSTabGroupPlugin']


class CMSDropdownTabPlugin(CMSPluginBase):
    allow_children = True
    child_classes = ['CMSTabPlugin']
    model = TabDropDownPlugin
    module = _('Tabs')
    name = _('Tab dropdown')
    parent_classes = ['CMSTabGroupPlugin']
    render_template = "aldryn_tabnav/tab.html"


plugin_pool.register_plugin(CMSDropdownTabPlugin)
plugin_pool.register_plugin(CMSTabGroupPlugin)
plugin_pool.register_plugin(CMSTabPlugin)
