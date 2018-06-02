from typing import List

from projects.entities.project import ProjectSchema
from projects.use_cases.abstract_projects_repository import AbstractProjectsRepository


class MongoProjectsRepository(AbstractProjectsRepository):
    def get(self) -> List[ProjectSchema]:
        pass
