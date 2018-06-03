from pymongo import MongoClient
from pytest import fixture

from projects.adapters.mongo_projects_repository import MongoProjectsRepository
from projects.entities.project import ProjectSchema


@fixture(scope='module')
def database():
    client = MongoClient(
        'mongodb://mongo:27017/',
        socketTimeoutMS=3000,
        connectTimeoutMS=3000,
        serverSelectionTimeoutMS=3000
    )
    client.drop_database('projects')

    db = client.projects
    collection = db.projects

    collection.insert_one({
        'id': 'a9c1fff4-09b1-4668-b94b-a301f21efdde',
        'title': 'some title',
        'description': 'some description',
        'status': 'some status',
        'links': {
            'homepage': 'https://some.url'
        }
    })


def test_get(database):
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
    repo = MongoProjectsRepository()

    actual_projects = repo.get()

    assert expected_projects == actual_projects
