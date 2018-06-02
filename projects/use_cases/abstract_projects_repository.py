from abc import ABC, abstractmethod
from typing import List

from projects.entities.project import ProjectSchema


class AbstractProjectsRepository(ABC):
    @abstractmethod
    def get(self) -> List[ProjectSchema]:
        pass
