import falcon
from falcon_cors import CORS

from projects.resources.healthcheck import HealthcheckResource
from projects.resources.projects import ProjectsResource

cors = CORS(allow_all_origins=True)
app = falcon.API(middleware=[cors.middleware])

app.add_route('/', HealthcheckResource)
app.add_route('/projects', ProjectsResource)
