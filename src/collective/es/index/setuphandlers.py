# -*- coding: utf-8 -*-
from Products.CMFPlone.interfaces import INonInstallable
from zope.interface import implementer


@implementer(INonInstallable)
class HiddenProfiles(object):

    def getNonInstallableProfiles(self):
        """Hide uninstall profile from site-creation and quickinstaller."""
        return [
            'collective.es.index:uninstall',
        ]


def post_install(context):
    """Post install script"""
    # we need to index the PloneSiteRoot as well in order to have it as a valid
    # parent

    # serializer = getMultiAdapter((obj, getRequest()), ISerializeToJson)

    # then - in theory - we would need to index all content. Just this is
    # probably expensive and may take a while. So we keep this a manual task.


def uninstall(context):
    """Uninstall script"""
    # Do something at the end of the uninstallation of this package.


def upgrade_to_1001(portal_setup):
    for step in ('plone.app.registry',
                 'controlpanel',):
        portal_setup.runImportStepFromProfile(
            'profile-collective.es.index:default',
            step,
            run_dependencies=False)
