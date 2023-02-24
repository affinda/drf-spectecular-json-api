from rest_framework_json_api.pagination import JsonApiPageNumberPagination

from drf_spectacular_jsonapi.schemas.plumbing import build_pagination_link


class JsonApiPageNumberPagination(JsonApiPageNumberPagination):

    def get_paginated_response_schema(self, schema):

        return {
            'type': 'object',
            'properties': {
                'data': {
                    "type": "array",
                    "items": schema
                },
                "links": {
                    "type": "object",
                    "properties": {
                        "first": build_pagination_link(self),
                        "last": build_pagination_link(self),
                        "prev": build_pagination_link(self),
                        "next": build_pagination_link(self),
                    }
                },
            },
            "required": ["data"],
        }
