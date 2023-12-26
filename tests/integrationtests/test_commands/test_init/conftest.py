import os

import pytest
import tempfile


@pytest.fixture()
def temp_dir():
    initial_dir = os.getcwd()
    try:
        temp_dir_path = tempfile.mkdtemp()
        os.chdir(temp_dir_path)
        yield temp_dir_path
    finally:
        os.chdir(initial_dir)
