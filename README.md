# Flask docs parser

## Requirements:

- Python 3.4+

## Installation and usage
```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
sh get_docs.sh
python parser.py
```

The above commands will make a virtual environment in a folder called `env` and install all the requirements listed in `requirements.txt` into that virtual environment.
Once that is done running `sh get_docs.sh` will `clone` the `git` repository of [pallets/flask](https://github.com/pallets/flask) and build the Flask HTML documentation using Sphinx.
Then running `python parser.py` will parse that documentation.
It will output a file called `data.json` which you can later use to your avail.

The output JSON file looks like this:
```json
[
    {
        "version": "2.0.x",
        "id": "flask.Flask.default_config",
        "title": "Flask.default_config",
        "permalink": "https://flask.palletsprojects.com/en/2.0.x/api/#flask.Flask.default_config",
        "categories": [
            "Flask"
        ],
        "default": "{'APPLICATION_ROOT': '/', 'DEBUG': None, 'ENV': None, 'EXPLAIN_TEMPLATE_LOADING': False, 'JSONIFY_MIMETYPE': 'application/json', 'JSONIFY_PRETTYPRINT_REGULAR': False, 'JSON_AS_ASCII': True, 'JSON_SORT_KEYS': True, 'MAX_CONTENT_LENGTH': None, 'MAX_COOKIE_SIZE': 4093, 'PERMANENT_SESSION_LIFETIME': datetime.timedelta(days31), 'PREFERRED_URL_SCHEME': 'http', 'PRESERVE_CONTEXT_ON_EXCEPTION': None, 'PROPAGATE_EXCEPTIONS': None, 'SECRET_KEY': None, 'SEND_FILE_MAX_AGE_DEFAULT': datetime.timedelta(seconds43200), 'SERVER_NAME': None, 'SESSION_COOKIE_DOMAIN': None, 'SESSION_COOKIE_HTTPONLY': True, 'SESSION_COOKIE_NAME': 'session', 'SESSION_COOKIE_PATH': None, 'SESSION_COOKIE_SAMESITE': None, 'SESSION_COOKIE_SECURE': False, 'SESSION_REFRESH_EACH_REQUEST': True, 'TEMPLATES_AUTO_RELOAD': None, 'TESTING': False, 'TRAP_BAD_REQUEST_ERRORS': None, 'TRAP_HTTP_EXCEPTIONS': False, 'USE_X_SENDFILE': False}",
        "content": "Default configuration parameters."
    }
]
```