# validate_json

Restful service to validate JSON docs against JSON schemas

### Prerequisities
 * Python 2.7
 * pip
 * virtualenv
 * virtualenvwrapper

### Installing && Running

* Clone project, `git clone git@github.com:oguzhanunlu/validate_json.git`
* Create a python2.7 virtual environment
* Inside environment, run `pip install -r requirements.txt`, to install depencencies.
* At the root of the project, start Django runserver, `python manage.py runserver`

Now server is up and running at 8000 port.

### API Endpoints

```
POST    /schema/SCHEMAID        - Upload JSON Schema with unique `SCHEMAID`
GET     /schema/SCHEMAID        - Download JSON Schema with unique `SCHEMAID`

POST    /validate/SCHEMAID      - Validate JSON document against the JSON Schema identified by `SCHEMAID`
```

### Use case 

User has a JSON file `config.json` as following:

```json
{
    "source": "/home/alice/image.iso",
    "destination": "/mnt/storage",
    "timeout": null,
    "chunks": {
        "size": 1024,
        "number": null
    }
}

```

And expects it conforms to the following JSON Schema `config-schema.json`, after cleaned from keys where value is None:

```json
{
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "source": {
            "type": "string"
        },
        "destination": {
            "type": "string"
        },
        "timeout": {
            "type": "integer",
            "minimum": 0,
            "maximum": 32767
        },
        "chunks": {
            "type": "object",
            "properties": {
                "size": {
                    "type": "integer"
                },
                "number": {
                    "type": "integer"
                }
            },
            "required": ["size"]
        }
    },
    "required": ["source", "destination"]
}

```

To check that it really fits the schema:

1. Upload the JSON Schema: `curl http://localhost/schema/config-schema -X POST -d @config-schema.json`
2. Response will be: `{"action": "uploadSchema", "id": "config-schema", "status": "success"}` and status code 201
3. Upload the JSON document to validate it `curl http://localhost/validate/config-schema -X POST -d @config.json`
4. Response will be: `{"action": "validateDocument", "id": "config-schema", "status": "success"}` and status code 200
