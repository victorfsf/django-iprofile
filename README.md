# Django IProfile

[![PyPI version](https://badge.fury.io/py/django-iprofile.svg)](https://badge.fury.io/py/django-iprofile)

A Django shell command to work with [IProfile](https://github.com/victorfsf/python-iprofile/).


## Installation

Install via pip:

```
pip install django-iprofile
```

Add `iprofile_shell` to your project's `INSTALLED_APPS`.

## Usage

See the IProfile [guide](https://github.com/victorfsf/python-iprofile/wiki/) and [command reference](https://github.com/victorfsf/python-iprofile/wiki/Command-Reference/) before using this.

##### Opening the shell:

```
$ python manage.py ishell <profile_name>
```

##### To open the [active IProfile](https://github.com/victorfsf/python-iprofile/wiki#activating-a-profile), run:

```
$ python manage.py ishell .
```
