<h1 align="center">
  <a href="https://github.com/{{ cookiecutter.github_profile }}/{{ cookiecutter.project_slug | replace("_", "-") }}">
    <img alt="{{ cookiecutter.project_name }}" src="{{ cookiecutter.project_slug }}.png" width="505">
  </a>
  <br> {{ cookiecutter.project_name }} - {{ cookiecutter.project_short_description }}<br>
</h1>

{% if cookiecutter.add_badges|lower == 'y' -%}
![Python package](https://github.com/{{ cookiecutter.github_profile }}/{{ cookiecutter.project_slug | replace("_", "-") }}/workflows/Python%20package/badge.svg)
[![Build Status](https://travis-ci.org/{{ cookiecutter.project_slug | replace("_", "-") }}/{{ cookiecutter.project_slug | replace("_", "-") }}.svg?branch=master)](https://travis-ci.org/{{ cookiecutter.project_slug | replace("_", "-") }}/{{ cookiecutter.project_slug | replace("_", "-") }})
![Docs](https://readthedocs.org/projects/{{ cookiecutter.project_slug | replace("_", "-") }}/badge/?version=latest)
{%- if cookiecutter.add_pyup_badge|lower == 'y' -%}
![Pyup](https://pyup.io/repos/github/{{ cookiecutter.project_slug | replace("_", "-") }}/{{ cookiecutter.project_slug | replace("_", "-") }}/shield.svg){% endif -%}
![PyPI - Wheel](https://img.shields.io/pypi/wheel/{{ cookiecutter.project_slug }})
![PyPI](https://img.shields.io/pypi/v/{{ cookiecutter.project_slug }})
![PyPI - Implementation](https://img.shields.io/pypi/implementation/{{ cookiecutter.project_slug }})
![PyPI - Downloads](https://img.shields.io/pypi/dm/{{ cookiecutter.project_slug }})
![PyPI - License](https://img.shields.io/pypi/l/{{ cookiecutter.project_slug }}){% endif -%}

<div align="center">
  <h4>
    | <a href="{{ cookiecutter.project_homepage }}">Website</a> |
    <a href="#features">Features</a> |
    <a href="#requirements">Requirements</a> |
    <a href="#installing">Install</a> |
    <a href="#donation">Donation</a> |
  </h4>
</div>

<div align="center">
  <sub>Built with ❤︎ by:
  <a href="{{ cookiecutter.author_website }}" target="_blank">{{ cookiecutter.your_full_name }}</a></sub>
</div>
<br>
<br>

{{ cookiecutter.project_short_description }}

{%- if cookiecutter.use_sponsor|lower == 'y' -%}
## Donation

If you liked my work, buy me a coffee :coffee: :smiley:

If you want to contribute to the project, click on the **Sponsor** button to access the donation forms.
{%- endif -%}

## License

The project is available as open source under the terms of the [MIT License](https://github.com/{{ cookiecutter.github_profile }}/{{ cookiecutter.project_slug | replace("_", "-") }}/blob/master/LICENSE) ©

## Credits

See, [AUTHORS](https://github.com/{{ cookiecutter.github_profile }}/{{ cookiecutter.project_slug | replace("_", "-") }}/blob/master/AUTHORS.rst).