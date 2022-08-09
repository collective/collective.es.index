Changelog
=========

1.0a2 (unreleased)
------------------

- Move to elasticsearch_dsl package for query generation

- Add celery support (requires latest collective.celery) tested with celery>=4.2.0

- Add new directives: max_blobsize, request_timeout, use_celery, indexed_chars

- No longer keeps the b64 encoded blob in ES index

- Add highlight support on search results

- basic plone 4 compatibility

- refactor code to avoid sending obj data in redis payload

- add stopgap solution for missing rid problem

- add a more detailed comment for code that skips highlights with no rid

- avoid generating index data twice for celery indexing, use relative path from root

- Retry on POSKeyError when using celery

- #2610885: Sleep for a few seconds in index task because retry isn't working
  with collective.celery tasks.
  [JL 2019-02-28]

- #2610885: Move sleep to before call to get_payload.
  [JL 2019-02-28]

- Support indexing blob fields on Archetypes based content types.
  [JL 2019-03-04]

- Pass the object url to the task.
  [JL 2019-03-04]

- Add control panel and allow user to configure the index name.
  [JL 2019-03-04]

- Don't swallow exceptions in the celery task.
  [JL 2019-03-04]

- #2610885: Remove sleep and restore retry on POSKeyError
  [JL 2019-03-04]

- #2698336: Retry index on TransportError.
  [JL 2019-04-22]

- Check blob sizes before extracting the blob data.
  [JL 2019-08-23]

- #2906253: Don't use scroll.
  [JL 2019-09-09]

- #3051653: Fix search infinite loop.
  [JL 2019-11-21]

- #2972719: Don't send query attribute to elasticsearch
  [JL 2019-11-22]

- Don't index an item if the index name hasn't been configured yet.
  [JL 2020-07-20]

- Allow the index name to be configured in the zope config.
  [JL 2020-07-20]

- Add package name to async task names.

- Allow customizations to index settings and mapping through adapters.

- Cleanup and reformat INITIAL_MAPPING


1.0a1 (git tag)
---------------

- Initial release.
  [jensens]
