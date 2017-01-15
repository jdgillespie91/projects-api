import json
import os

import falcon
from falcon_cors import CORS

from projects import __version__


cors = CORS(allow_all_origins=True)

response = [
    {
        'objectId': 0,
        'title': 'trackerSpend',
        'url': 'https://github.com/jdgillespie91/trackerSpend',
        'status': 2,
    },
    {
        'objectId': 1,
        'title': 'graphs',
        'url': 'https://github.com/jdgillespie91/graphs',
        'status': 3,
    },
    {
        'objectId': 2,
        'title': 'jakegillespie.me',
        'url': 'https://github.com/jdgillespie91/jakegillespie.me',
        'status': 1,
    },
]


class ProjectsResource(object):
    def on_get(self, req, resp):
        resp.body = json.dumps(response)


class HealthcheckResource(object):
    def on_get(self, req, resp):
        env = os.environ.get('PROJECT_ENV', 'prod')
        version = __version__

        resp.append_header('Version', f'{env}-{version}')
        resp.body = json.dumps('Hello, world!')


app = falcon.API(middleware=[cors.middleware])

projects_resource = ProjectsResource()
app.add_route('/projects', projects_resource)

healthcheck = HealthcheckResource()
app.add_route('/', healthcheck)
