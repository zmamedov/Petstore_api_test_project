from pathlib import Path

import petstore_api_test_project


def abs_path_from_project(file_name):
    return str(Path(petstore_api_test_project.__file__).parent.parent.joinpath(file_name))
