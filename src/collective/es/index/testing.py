# -*- coding: utf-8 -*-
from __future__ import absolute_import
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import collective.es.index


class CollectiveEsIndexLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=collective.es.index)
        z2.installProduct(app, 'collective.es.index')

    def setUpPloneSite(self, portal):
        # provide an ES connection
        from collective.es.index.interfaces import IElasticSearchClient
        from elasticsearch import Elasticsearch
        from zope.component import provideUtility
        from zope.interface import directlyProvides
        es = Elasticsearch(
            [{'host': '127.0.0.1', 'port': '9200'}],
            use_ssl=False,
        )
        directlyProvides(es, IElasticSearchClient)
        provideUtility(es)


COLLECTIVE_ES_INDEX_FIXTURE = CollectiveEsIndexLayer()


COLLECTIVE_ES_INDEX_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_ES_INDEX_FIXTURE,),
    name='CollectiveEsIndexLayer:IntegrationTesting',
)


COLLECTIVE_ES_INDEX_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_ES_INDEX_FIXTURE,),
    name='CollectiveEsIndexLayer:FunctionalTesting',
)


COLLECTIVE_ES_INDEX_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        COLLECTIVE_ES_INDEX_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='CollectiveEsIndexLayer:AcceptanceTesting',
)
