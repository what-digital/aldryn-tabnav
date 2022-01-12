from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify

from cms.models import CMSPlugin

from .conf import settings


class TabGroupPlugin(CMSPlugin):
    tab_group_name = models.CharField(max_length=200, blank=False)
    layout_template = models.CharField(
        verbose_name=_('layout'),
        max_length=200,
        choices=settings.ALDRYN_TABNAV_TEMPLATES,
        default=settings.ALDRYN_TABNAV_DEFAULT_TEMPLATE,
    )

    def __unicode__(self):
        return self.tab_group_name or unicode(self.pk)


class TabPlugin(CMSPlugin):
    tab_title = models.CharField(verbose_name=_('title'), max_length=127)
    tab_extra_icon = models.CharField(
        verbose_name=_('icon css class'),
        max_length=63,
        choices=settings.ALDRYN_TABNAV_ICONS,
        blank=True,
    )

    def __unicode__(self):
        return self.tab_title

    def tab_html_id(self):
        html_id = '%d-%s' % (self.pk, self.tab_title)
        return slugify(html_id)

    def tab_icon_class(self):
        icon_class = 'icon icon-{0}'
        return icon_class.format(self.tab_extra_icon)


class TabDropDownPlugin(CMSPlugin):
    # used in template to distinguish between normal and dropdown tabs
    is_dropdown = True

    tab_title = models.CharField(verbose_name=_('title'), max_length=127)

    def __unicode__(self):
        return self.tab_title

    def tab_html_id(self):
        html_id = '%d-%s' % (self.pk, self.tab_title)
        return slugify(html_id)
