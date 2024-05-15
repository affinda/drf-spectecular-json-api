from django.utils.translation import gettext_lazy as _
from rest_framework.fields import empty
from rest_framework_json_api import serializers
from rest_framework_json_api.utils import (format_field_name,
                                           get_related_resource_type,
                                           get_resource_type_from_serializer)


def build_pagination_link(pagination):
    return {
        "type": "string",
        "format": "uri",
        "nullable": True,  # TODO: only in OpenApi 3.0.x,
        "example": f"http://api.example.org/resource_path/?{pagination.page_query_param}=4&{pagination.page_size_query_param}=10",
    }


def build_json_api_relationship_object(field):
    schema = {
        "type": "object",
        "properties": {
            "id": {
                "type": "string",
                # TODO: could also provide the correct id format
                "description": _("The identifier of the related object.")
            },
            "type": {
                "type": "string",
                "description": _(""),
                "enum": [get_related_resource_type(field)]
            }
        },
        "required": ["id", "type"],
    }

    if field.read_only:
        schema["readOnly"] = True
    if field.write_only:
        schema["writeOnly"] = True
    if field.allow_null:
        schema["nullable"] = True
    if field.default and field.default != empty:
        schema["default"] = field.default
    if field.help_text:
        # Ensure django gettext_lazy is rendered correctly
        schema["description"] = str(field.help_text)

    return schema


def build_json_api_data_frame(schema):
    return {
        "type": "object",
        "properties": {
            "data": schema
        },
    }
