import pytest
from tortoise.contrib.test import finalizer
from tortoise.contrib.test import initializer


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    test_fn = item.obj
    docstring = getattr(test_fn, "__doc__")
    if docstring:
        report.nodeid = docstring


@pytest.fixture(scope="session", autouse=True)
def initialize_tests(request):
    initializer(["src.core.models.entities"], db_url=None, app_label="models")

    request.addfinalizer(finalizer)
