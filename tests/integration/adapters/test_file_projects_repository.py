from pathlib import Path

from projects.adapters.file_projects_repository import FileProjectsRepository
from projects.entities.project import ProjectSchema


def test_get():
    expected_projects = [
        ProjectSchema().load({
            'id': 'a9c1fff4-09b1-4668-b94b-a301f21efdde',
            'title': 'some title',
            'description': 'some description',
            'status': 'some status',
            'links': {
                'homepage': 'https://some.url'
            }
        })
    ]
    repo = FileProjectsRepository(file=Path('data/test_projects.csv'))

    actual_projects = repo.get()

    assert expected_projects == actual_projects
