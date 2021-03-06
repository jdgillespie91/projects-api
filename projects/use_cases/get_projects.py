from typing import List

from projects.entities.project import ProjectSchema
from projects.use_cases.abstract_projects_repository import AbstractProjectsRepository


def get_projects(projects_repository: AbstractProjectsRepository) -> List[ProjectSchema]:
    return projects_repository.get()
