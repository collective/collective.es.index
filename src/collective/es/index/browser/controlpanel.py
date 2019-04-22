# -*- coding: utf-8 -*-
from .. import _
from ..interfaces import ICollectiveESIndexSettings
from plone import api
from plone.app.registry.browser import controlpanel


class CollectiveESIndexSettingsEditForm(controlpanel.RegistryEditForm):

    schema = ICollectiveESIndexSettings
    label = _(u'Elasticsearch Settings')
    description = _('')

    def updateWidgets(self):
        super(CollectiveESIndexSettingsEditForm, self).updateWidgets()
        index_name_widget = self.widgets.get('index_name', None)
        settings = self.getContent()
        if index_name_widget is not None and not settings.index_name:
            portal = api.portal.get()
            name = 'plone_{0}'.format(portal.getId()).lower()
            index_name_widget.value = name


class CollectiveESIndexSettingsControlPanel(controlpanel.ControlPanelFormWrapper):
    form = CollectiveESIndexSettingsEditForm
