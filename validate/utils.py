# -*- coding: utf-8 -*-

import jsonschema
import sys

def clean_doc(doc):
    """
    Clean given JSON document from keys where its value is None
    :param doc: Pure, dirty JSON
    :return: Cleaned JSON document
    """
    for key, value in list(doc.items()):
        if value is None:
            del doc[key]
        elif isinstance(value, dict):
            clean_doc(value)
    return doc


def is_valid(doc, schema):
    """
    Checks if given doc is valid against given schema
    :param doc: to be validated JSON
    :param schema: base JSON
    :return: a boolean result and error
    """
    try:
        jsonschema.validate(doc, schema)
        sys.stdout.write("OK\n")
        return True, None

    except jsonschema.exceptions.ValidationError as val_err:
        sys.stderr.write("FAIL\n")
        return False, val_err
