from pytest import fixture

from search import create_app


@fixture
def app():
    _app = create_app(testing=True)
    return _app


@fixture
def client(app):
    return app.test_client()
