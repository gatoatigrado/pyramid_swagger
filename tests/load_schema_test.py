# -*- coding: utf-8 -*-
"""
Unit tests for load_schema().
"""

from pyramid_swagger.load_schema import extract_body_schema


def test_extract_body_schema_with_ref():
    """Tests extract_body_schema's handling of $ref things."""
    sample_schema = {
        'parameters': [{
            'paramType': 'body',
            '$ref': 'CatfoodModel'
        }]
    }
    schema = extract_body_schema(sample_schema, NotImplemented)
    assert schema == {'$ref': 'CatfoodModel'}


def test_extract_body_schema_docstring_example():
    docstring_example = {'parameters': [{
        "paramType": "body",
        "name": "body",
        "description": "json list: [ll1,ll2]",
        "type": "array",
        "items": {
            "$ref": "GeoPoint"
        },
        "required": True
    }]}
    models = {'GeoPoint': NotImplemented}
    schema = extract_body_schema(docstring_example, models)
    assert schema == {
        'items': {'$ref': 'GeoPoint'},
        'required': True,
        'type': 'array',
        'description': 'json list: [ll1,ll2]'
    }