from csv import DictReader
from pathlib import Path
from typing import List, Dict

from projects.entities.project import ProjectSchema
from projects.use_cases.abstract_projects_repository import AbstractProjectsRepository


class FileProjectsRepository(AbstractProjectsRepository):
    def __init__(self, file: Path) -> None:
        self._file = file
        self._schema = ProjectSchema()

    def get(self) -> List[ProjectSchema]:
        with open(self._file) as f:
            return list(map(self._load, DictReader(f)))

    def _load(self, data: Dict) -> ProjectSchema:
        data['links'] = {'homepage': data['homepage']}
        del data['homepage']

        project = self._schema.load(data)  # type: ProjectSchema
        return project
