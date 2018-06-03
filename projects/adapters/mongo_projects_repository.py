from typing import List, Dict

from pymongo import MongoClient

from projects.entities.project import ProjectSchema
from projects.use_cases.abstract_projects_repository import AbstractProjectsRepository


class MongoProjectsRepository(AbstractProjectsRepository):
    def __init__(self) -> None:
        self._schema = ProjectSchema()

    def get(self) -> List[ProjectSchema]:
        client = MongoClient(
            'mongodb://mongo:27017/',
            socketTimeoutMS=3000,
            connectTimeoutMS=3000,
            serverSelectionTimeoutMS=3000
        )
        database = client.projects
        collection = database.projects

        return list(map(self._load, collection.find()))

    def _load(self, data: Dict) -> ProjectSchema:
        project = self._schema.load(data)  # type: ProjectSchema
        return project
