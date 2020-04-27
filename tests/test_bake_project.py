from tests.base_config import run_inside_dir, bake_in_temp_dir


def test_pytest_cookies(cookies):
    result = cookies.bake()
    assert result.exit_code == 0
    assert result.exception is None


def test_bake_with_defaults(cookies):
    with bake_in_temp_dir(cookies) as result:
        assert result.project.isdir()
        assert result.exit_code == 0
        assert result.exception is None
        found_toplevel_files = [f.basename for f in result.project.listdir()]
        print(found_toplevel_files)
        assert 'README.md' in found_toplevel_files


def test_using_pytest(cookies):
    with bake_in_temp_dir(cookies, extra_context={'use_pytest': 'y'}) as result:
        assert result.project.isdir()
        test_file_path = result.project.join(
            'tests/test_cookiecutter_python_package.py'
        )
        lines = test_file_path.readlines()
        assert "import pytest" in ''.join(lines)
        assert run_inside_dir('pytest', str(result.project)) == 0


def test_not_using_pytest(cookies):
    with bake_in_temp_dir(cookies, extra_context={'use_pytest': 'n'}) as result:
        assert result.project.isdir()
        test_file_path = result.project.join(
            'tests/test_cookiecutter_python_package.py'
        )
        lines = test_file_path.readlines()
        assert "import unittest" in ''.join(lines)
        assert "import pytest" not in ''.join(lines)
        assert run_inside_dir('python -m unittest tests/test_cookiecutter_python_package.py', str(result.project)) == 0


def test_using_poetry(cookies):
    with bake_in_temp_dir(cookies, extra_context={'use_poetry': 'y'}) as result:
        test_file_path = result.project.join(
            'pyproject.toml'
        )
        lines = test_file_path.readlines()
        assert "[tool.poetry]" in ''.join(lines)
        assert run_inside_dir('poetry build', str(result.project)) == 0


def test_not_using_poetry(cookies):
    with bake_in_temp_dir(cookies, extra_context={'use_poetry': 'n'}) as result:
        test_file_path = result.project.join(
            'setup.py'
        )
        lines = test_file_path.readlines()
        assert "from setuptools import setup, find_packages" in ''.join(lines)
        assert run_inside_dir('python setup.py test', str(result.project)) == 0
