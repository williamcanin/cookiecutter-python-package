# Cookiecutter Python Package

![Python package](https://github.com/williamcanin/cookiecutter-python-package/workflows/Python%20package/badge.svg)

With **Cookiecutter Python Package**, you can create your Python packages with a professional structure and with a lot of resources available.

Pypkg Cookiecutter is a template inspired by the [Cookiecutter Pypackage](https://github.com/audreyr/cookiecutter-pypackage).

## Requirements

| Required        | Required version    |   How to verify     | How to install  |
| --------------- | ------------------- | ------------------- | --------------- |
| Git             |   >= 2.25.0         | `git --version`     | [Git](http://git-scm.com/) |
| Python          |   >= 3.8            | `python --version`  | [Python](https://www.python.org/about/gettingstarted/) |
| Black           |   >= 19.10b0        | `black --version`   | [Black](https://pypi.org/project/black/) |
| Cookiecutter    |   >= 1.7            | `cookiecutter --version` | [Cookiecutter](https://pypi.org/project/cookiecutter/) |
| Pip             |   >= 20.0.2         | `pip --version`    | [Pip](https://pip.pypa.io/en/stable/installing/) |
| *Poetry         |   >= 1.0.5          | `poetry --version`     | [Poetry](https://python-poetry.org/docs/#installation) |


\* If chosen at creation

## Using:

```
$ pip install cookiecutter --user
$ cookiecutter https://github.com/williamcanin/cookiecutter-python-package.git
```
After that, go to the folder with the name of the project that you entered at the time of the questions. Example:

```
$ cd my_package
```

**Create the virtual machine, activate it and install the requirements:**

```
$ python -m venv venv
$ . venv/bin/activate
$ pip install --upgrade pip
$ pip install -r requeriments_dev.txt requeriments.txt
```

or

**Create the virtual machine, activate it and install the requirements using Poetry:**

```
$ poetry shell
$ poetry install
```

There, you can start to develop your Python package.

## Developers of Cookiecutter Python Package

If you want to build something more in this project, prepare the environment like this:

```
$ git clone https://github.com/williamcanin/cookiecutter-python-package.git
$ cd cookiecutter-python-package
$ python -m venv venv
$ . venv/bin/activate
$ pip install --upgrade pip
$ pip install -r requirements.txt
```

**Tests**

```
$ tox
```

## License

The gem is available as open source under the terms of the [MIT License](https://github.com/williamcanin/cookiecutter-python-package/blob/master/LICENSE).
