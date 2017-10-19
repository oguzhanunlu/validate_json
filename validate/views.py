# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

import json

from .utils import clean_doc, is_valid


@csrf_exempt
def index(request):

    if request.method == 'POST':
        unique_id = request.path.split('/')[-1]
        doc = json.loads(request.body)
        doc = clean_doc(doc)

        with open('static/' + unique_id + '.json', 'r') as f:
            schema = json.load(f)

        valid, err = is_valid(doc, schema)

        if valid:
            response = JsonResponse({"action": "validateDocument",
                                     "id": unique_id,
                                     "status": "success"
                                     })
        else:
            response = JsonResponse({"action": "validateDocument",
                                     "id": unique_id,
                                     "status": "error",
                                     "message": err,
                                     })

    return response
