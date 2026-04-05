import os
import pytest
from src import app

@pytest.fixture(scope= 'module')
def test_client():
    os.environ['CONFIG_TYPE'] = 'config.TestingConfig'
    myapp = app.create_app()
    # other setup can go here

    with myapp.test_client() as testing_client:
        with myapp.app_context():
            yield testing_client
