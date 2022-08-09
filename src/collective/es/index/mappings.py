INITIAL_MAPPING = {
    u'content': {
        u'properties': {
            u'@id': {
                u'fields': {u'keyword': {u'ignore_above': 256,
                                       u'type': u'keyword'}},
                u'type': u'text'},
            u'@type': {
                u'fields': {u'keyword': {u'ignore_above': 256,
                                       u'type': u'keyword'}},
                u'type': u'text'},
            u'UID': {
                u'fields': {u'keyword': {u'ignore_above': 256,
                                       u'type': u'keyword'}},
                u'type': u'text'},
            u'allow_discussion': {
                u'type': u'boolean'},
            u'changeNote': {
                u'fields': {u'keyword': {u'ignore_above': 256,
                                       u'type': u'keyword'}},
                u'type': u'text'},
            u'created': {
                u'type': u'date'},
            u'creators': {
                u'fields': {u'keyword': {u'ignore_above': 256,
                                       u'type': u'keyword'}},
                u'type': u'text'},
            u'description': {
                u'fields': {u'keyword': {u'ignore_above': 256,
                                       u'type': u'keyword'}},
                u'type': u'text'},
            u'effective': {
                u'type': u'date'},
            u'exclude_from_nav': {
                u'type': u'boolean'},
            u'extracted_file': {
                u'properties': {
                    u'author': {u'fields': {u'keyword': {u'ignore_above': 256,
                                                      u'type': u'keyword'}},
                               u'type': u'text'},
                    u'content': {u'fields': {u'keyword': {u'ignore_above': 256,
                                                       u'type': u'keyword'}},
                                u'type': u'text'},
                    u'content_length': {u'type': u'long'},
                    u'content_type': {u'fields': {u'keyword': {u'ignore_above': 256,
                                                            u'type': u'keyword'}},
                                     u'type': u'text'},
                    u'date': {u'type': u'date'},
                    u'keywords': {u'fields': {u'keyword': {u'ignore_above': 256,
                                                        u'type': u'keyword'}},
                                 u'type': u'text'},
                    u'language': {u'fields': {u'keyword': {u'ignore_above': 256,
                                                        u'type': u'keyword'}},
                                 u'type': u'text'},
                    u'title': {u'fields': {u'keyword': {u'ignore_above': 256,
                                                     u'type': u'keyword'}},
                              u'type': u'text'}}},
            u'extracted_image': {
                u'properties': {
                    u'content_length': {u'type': u'long'},
                    u'content_type': {u'fields': {u'keyword': {u'ignore_above': 256,
                                                            u'type': u'keyword'}},
                                     u'type': u'text'}}},
            u'extracted_text': {
                u'properties': {
                    u'content': {u'fields': {u'keyword': {u'ignore_above': 256,
                                                       u'type': u'keyword'}},
                                u'type': u'text'},
                    u'content_length': {u'type': u'long'},
                    u'content_type': {u'fields': {u'keyword': {u'ignore_above': 256,
                                                            u'type': u'keyword'}},
                                     u'type': u'text'},
                    u'language': {u'fields': {u'keyword': {u'ignore_above': 256,
                                                        u'type': u'keyword'}},
                                 u'type': u'text'}}},
            u'file_meta': {
                u'properties': {
                    u'content-type': {u'fields': {u'keyword': {u'ignore_above': 256,
                                                            u'type': u'keyword'}},
                                     u'type': u'text'},
                    u'download': {u'fields': {u'keyword': {u'ignore_above': 256,
                                                        u'type': u'keyword'}},
                                 u'type': u'text'},
                    u'filename': {u'fields': {u'keyword': {u'ignore_above': 256,
                                                        u'type': u'keyword'}},
                                 u'type': u'text'},
                    u'size': {u'type': u'long'}}},
            u'height': {
                u'type': u'long'},
            u'id': {
                u'fields': {u'keyword': {u'ignore_above': 256,
                                       u'type': u'keyword'}},
                u'type': u'text'},
            u'image_meta': {
                u'properties': {
                    u'content-type': {u'fields': {u'keyword': {u'ignore_above': 256,
                                                            u'type': u'keyword'}},
                                     u'type': u'text'},
                    u'download': {u'fields': {u'keyword': {u'ignore_above': 256,
                                                        u'type': u'keyword'}},
                                 u'type': u'text'},
                    u'filename': {u'fields': {u'keyword': {u'ignore_above': 256,
                                                        u'type': u'keyword'}},
                                 u'type': u'text'},
                    u'height': {u'type': u'long'},
                    u'scales': {u'properties': {u'icon': {u'properties': {
                        u'download': {u'fields': {u'keyword': {u'ignore_above': 256,
                                                            u'type': u'keyword'}},
                                     u'type': u'text'},
                        u'height': {u'type': u'long'},
                        u'width': {u'type': u'long'}}},
                        u'large': {u'properties': {u'download': {
                            u'fields': {
                                u'keyword': {u'ignore_above': 256,
                                            u'type': u'keyword'}},
                            u'type': u'text'},
                            u'height': {
                                u'type': u'long'},
                            u'width': {
                                u'type': u'long'}}},
                        u'listing': {u'properties': {u'download': {
                            u'fields': {
                                u'keyword': {u'ignore_above': 256,
                                            u'type': u'keyword'}},
                            u'type': u'text'},
                            u'height': {
                                u'type': u'long'},
                            u'width': {
                                u'type': u'long'}}},
                        u'mini': {u'properties': {u'download': {
                            u'fields': {
                                u'keyword': {u'ignore_above': 256,
                                            u'type': u'keyword'}},
                            u'type': u'text'},
                            u'height': {
                                u'type': u'long'},
                            u'width': {
                                u'type': u'long'}}},
                        u'preview': {u'properties': {u'download': {
                            u'fields': {
                                u'keyword': {u'ignore_above': 256,
                                            u'type': u'keyword'}},
                            u'type': u'text'},
                            u'height': {
                                u'type': u'long'},
                            u'width': {
                                u'type': u'long'}}},
                        u'thumb': {u'properties': {u'download': {
                            u'fields': {
                                u'keyword': {u'ignore_above': 256,
                                            u'type': u'keyword'}},
                            u'type': u'text'},
                            u'height': {
                                u'type': u'long'},
                            u'width': {
                                u'type': u'long'}}},
                        u'tile': {u'properties': {u'download': {
                            u'fields': {
                                u'keyword': {u'ignore_above': 256,
                                            u'type': u'keyword'}},
                            u'type': u'text'},
                            u'height': {
                                u'type': u'long'},
                            u'width': {
                                u'type': u'long'}}}}},
                    u'size': {u'type': u'long'},
                    u'width': {u'type': u'long'}}},
            u'is_folderish': {
                u'type': u'boolean'},
            u'item_count': {
                u'type': u'long'},
            u'language': {
                u'fields': {u'keyword': {u'ignore_above': 256,
                                       u'type': u'keyword'}},
                u'type': u'text'},
            u'layout': {
                u'fields': {u'keyword': {u'ignore_above': 256,
                                       u'type': u'keyword'}},
                u'type': u'text'},
            u'limit': {
                u'type': u'long'},
            u'metadata': {
                u'fields': {u'keyword': {u'ignore_above': 256,
                                       u'type': u'keyword'}},
                u'type': u'text'},
            u'modified': {
                u'type': u'date'},
            u'nextPreviousEnabled': {
                u'type': u'boolean'},
            u'relatedItems': {
                u'properties': {
                    u'@id': {u'fields': {u'keyword': {u'ignore_above': 256,
                                                   u'type': u'keyword'}},
                            u'type': u'text'},
                    u'@type': {u'fields': {u'keyword': {u'ignore_above': 256,
                                                     u'type': u'keyword'}},
                              u'type': u'text'},
                    u'description': {u'fields': {u'keyword': {u'ignore_above': 256,
                                                           u'type': u'keyword'}},
                                    u'type': u'text'},
                    u'review_state': {u'fields': {u'keyword': {u'ignore_above': 256,
                                                            u'type': u'keyword'}},
                                     u'type': u'text'},
                    u'title': {u'fields': {u'keyword': {u'ignore_above': 256,
                                                     u'type': u'keyword'}},
                              u'type': u'text'}}},
            u'retrieve_thumb': {
                u'type': u'boolean'},
            u'review_state': {
                u'fields': {u'keyword': {u'ignore_above': 256,
                                       u'type': u'keyword'}},
                u'type': u'text'},
            u'rid': {
                u'type': u'long'},
            u'rights': {
                u'fields': {u'keyword': {u'ignore_above': 256,
                                       u'type': u'keyword'}},
                u'type': u'text'},
            u'table_of_contents': {
                u'type': u'boolean'},
            u'text_meta': {
                u'properties': {
                    u'content-type': {u'fields': {u'keyword': {u'ignore_above': 256,
                                                            u'type': u'keyword'}},
                                     u'type': u'text'},
                    u'data': {u'fields': {u'keyword': {u'ignore_above': 256,
                                                    u'type': u'keyword'}},
                             u'type': u'text'},
                    u'encoding': {u'fields': {u'keyword': {u'ignore_above': 256,
                                                        u'type': u'keyword'}},
                                 u'type': u'text'}}},
            u'title': {
                u'fields': {u'keyword': {u'ignore_above': 256,
                                       u'type': u'keyword'}},
                u'type': u'text'},
            u'version': {
                u'fields': {u'keyword': {u'ignore_above': 256,
                                       u'type': u'keyword'}},
                u'type': u'text'},
            u'versioning_enabled': {
                u'type': u'boolean'},
            u'width': {
                u'type': u'long'}}}}
