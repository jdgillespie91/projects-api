from pathlib import Path

from falcon import Request, Response

from projects.adapters.file_projects_repository import FileProjectsRepository
from projects.entities.project import ProjectSchema
from projects.use_cases.get_projects import get_projects


class ProjectsResource:
    @staticmethod
    def on_get(_: Request, resp: Response) -> None:
        projects = get_projects(FileProjectsRepository(file=Path('data/projects.csv')))
        resp.body = ProjectSchema(many=True).dumps(projects)
