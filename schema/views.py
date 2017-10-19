# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

import json


@csrf_exempt
def index(request):
    # print json.dumps(json.loads(request.body), indent=4, sort_keys=True)
    if request.method == 'GET':
        print "asdasd"
    elif request.method == 'POST':
        unique_id = request.path.split('/')[-1]
        schema = json.loads(request.body)

        with open('static/main.json', 'w') as f:
            json.dump(schema, f, indent=4)


    response = JsonResponse({"action": "uploadSchema", "id": unique_id, "status": "success"})
    return response

