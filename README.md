# pytest-checkipdb

[![pypi](https://img.shields.io/pypi/v/pytest-checkipdb.svg)](https://pypi.python.org/pypi/pytest-checkipdb/)
[![Downloads](https://pepy.tech/badge/pytest-checkipdb)](https://pepy.tech/project/pytest-checkipdb)
[![See Build Status on Travis CI](https://travis-ci.org/avallbona/pytest-checkipdb.svg?branch=master)](https://travis-ci.org/avallbona/pytest-checkipdb)
[![Hit counter](http://hits.dwyl.com/avallbona/pytest-checkipdb.svg)](http://hits.dwyl.com/avallbona/pytest-checkipdb)
[![Python package](https://github.com/avallbona/pytest-checkipdb/workflows/Python%20package/badge.svg?branch=master)](https://github.com/avallbona/pytest-checkipdb/actions)

Plugin to check if there are ipdb/pdb breakpoints left into our code

## Installation

You can install "pytest-checkipdb" via [pip](https://pypi.python.org/pypi/pip/) from [PyPI](https://pypi.python.org/pypi):

```bash
$ pip install pytest-checkipdb
```
## Usage

```bash
$ pytest --cipdb
```

## Contributing

Contributions are very welcome. Tests can be run with [tox](https://tox.readthedocs.io/en/latest/), please ensure
the coverage at least stays the same before you submit a pull request.

## Local development

Install all the python interpreters you need via [pyenv](https://github.com/pyenv/pyenv). E.g.:

```bash
$ pyenv install 3.5.3 
$ pyenv install 3.6.3 
$ pyenv install 3.7.7 
$ pyenv install 3.8.3
```

and then make them global with:

```bash
$ pyenv global 3.5.3 3.6.3 3.7.7 3.8.3
```

Run the tests

```bash
$ tox
```


## License

Distributed under the terms of the [MIT](http://opensource.org/licenses/MIT) license, **pytest-checkipdb** is free and open source software


## Issues

If you encounter any problems, please [file an issue](https://github.com/avallbona/pytest-checkipdb/issues) along with a detailed description.

------

This is a [Pytest](https://github.com/pytest-dev/pytest) plugin was generated with [Cookiecutter](https://github.com/audreyr/cookiecutter) along with [@hackebrot](https://github.com/hackebrot)'s [Cookiecutter-pytest-plugin](https://github.com/pytest-dev/cookiecutter-pytest-plugin) template.
