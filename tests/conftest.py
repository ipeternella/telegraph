import pytest
from tortoise.contrib.test import finalizer
from tortoise.contrib.test import initializer

from src.settings import DATABASE_TESTING_CONNECTION_URI


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Allows tests docstrings to be printed instead of the test function names when pytest
    is invoked, at least, with `-v` parameter (verbosity).
    """
    outcome = yield
    report = outcome.get_result()

    test_fn = item.obj
    docstring = getattr(test_fn, "__doc__")
    if docstring:
        report.nodeid = docstring


@pytest.fixture(scope="session", autouse=True)
def initialize_tests(request):
    """
    Prepares the test session's setup and teardown according to Tortoise ORM's requirements:

    More at: https://tortoise-orm.readthedocs.io/en/latest/contrib/unittest.html
    """
    # databases - tortoise orm: creates and drops a db with prefix 'test_'
    db_url = DATABASE_TESTING_CONNECTION_URI

    # initializes tortoise orm with testing features and drops and creates 'test_{}'db
    # also runs all models migrations due to 'Tortoise.generate_schemas()' call
    initializer(["src.core.models.entities"], db_url=db_url, app_label="models")

    # drops created 'test_{}' databases due to 'Tortoise._drop_databases()' call
    request.addfinalizer(finalizer)
