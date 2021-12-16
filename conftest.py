def pytest_addoption(parser):
    parser.addoption(
        "--name",
        action="append",
        default=[],
        help="list of persons names to test data integrity",
    )


def pytest_generate_tests(metafunc):
    if "name" in metafunc.fixturenames:
        metafunc.parametrize("name", metafunc.config.getoption("name"))
