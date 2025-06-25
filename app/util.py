import pathlib


def project_root() -> pathlib.Path:
    return pathlib.Path(__file__).parent.parent
