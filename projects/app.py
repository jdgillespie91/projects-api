import json

import falcon


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
        """Handles GET requests"""
        resp.status = falcon.HTTP_200  # This is the default status
        resp.body = json.dumps(response)


class HealthcheckResource(object):
    def on_get(self, req, resp):
        pass


app = falcon.API()

projects = ProjectsResource()
app.add_route('/projects', projects)

healthcheck = HealthcheckResource()
app.add_route('/', healthcheck)
