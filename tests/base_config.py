# NOTE: Before testing, update the pip: pip install --upgrade pip

import os
import subprocess
import shlex
from contextlib import contextmanager


@contextmanager
def inside_dir(dirpath):
    """
    Execute code from inside the given directory
    :param dirpath: String, path of the directory the command is being run.
    """
    old_path = os.getcwd()
    try:
        os.chdir(dirpath)
        yield
    finally:
        os.chdir(old_path)


def run_inside_dir(command, dirpath):
    """
    Run a command from inside a given directory, returning the exit status
    :param command: Command that will be executed
    :param dirpath: String, path of the directory the command is being run.
    """
    with inside_dir(dirpath):
        return subprocess.check_call(shlex.split(command))


@contextmanager
def bake_in_temp_dir(cookies, *args, **kwargs):
    import cookiecutter

    result = cookies.bake(*args, **kwargs)
    try:
        yield result
    finally:
        cookiecutter.utils.rmtree(str(result.project))
