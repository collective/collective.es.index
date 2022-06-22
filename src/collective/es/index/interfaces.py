# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""
from . import _
from zope import schema
from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer

try:
    from Products.CMFCore.interfaces import IIndexQueueProcessor
except ImportError:
    from collective.indexing.interfaces import IIndexQueueProcessor


class ICollectiveEsIndexLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""
    # unused, keep for BBB or future use


class IElasticSearchIndexQueueProcessor(IIndexQueueProcessor):
    """An index queue processor for elasticsearch."""


class IElasticSearchClient(Interface):
    """an initializd  python ElasticSearch object"""


class ICollectiveESIndexSettings(Interface):

    index_name = schema.TextLine(
        title=_(u'Index Name'),
        description=_(
            u'help_index_name',
            default=u'The name of the elasticsearch index used for the site.'
        ),
    )


class IAdditionalESIndexSettings(Interface):
    """ Interface for registering an adapter that returns a dict with settings
        to pass as the body during index creation.
    """


class IESIndexMapping(Interface):
    """ Interface for registering an adapter that returns a mapping dict to be
        used instead of mappings.INITIAL_MAPPING
    """
