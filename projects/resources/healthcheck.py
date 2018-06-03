import os

from falcon import Request, Response

from projects import __version__


class HealthcheckResource:
    @staticmethod
    def on_get(_: Request, resp: Response) -> None:
        env = os.environ.get('PROJECT_ENV', 'local')
        version = __version__

        resp.append_header('Version', f'{env}-{version}')
        resp.body = 'Hello, world!\n'
