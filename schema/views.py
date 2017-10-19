# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

import json


@csrf_exempt
def index(request):
    if request.method == 'GET':
        unique_id = request.path.split('/')[-1]
        with open('static/' + unique_id + '.json', 'r') as f:
            schema = json.load(f)

        return JsonResponse(schema)

    elif request.method == 'POST':
        unique_id = request.path.split('/')[-1]
        schema = json.loads(request.body)

        with open('static/' + unique_id + '.json', 'w') as f:
            json.dump(schema, f, indent=4)

    response = JsonResponse({"action": "uploadSchema",
                             "id": unique_id,
                             "status": "success"})
    return response
