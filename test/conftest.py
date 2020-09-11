import os

import pytest
import rose


@pytest.fixture()
def rose_client():
    clt = rose.Client(os.environ["token"])
    yield clt