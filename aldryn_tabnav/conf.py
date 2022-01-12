from django.conf import settings  # NOQA

from appconf import AppConf


class TabNavConf(AppConf):
    TEMPLATES = (
        ('aldryn_tabnav/tabgroup.html', 'aldryn_tabnav/tabgroup.html'),
    )
    DEFAULT_TEMPLATE = TEMPLATES[0][0]
    # empty choices will allow arbitrary values to be set in the form
    ICONS = (
    )
