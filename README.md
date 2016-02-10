# Django IProfile

A Django app adapting the Django shell to work with [IProfile](https://github.com/victorfsf/python-iprofile/)


## Installation

Install via pip:

```
pip install django-iprofile
```

Add `iprofile_shell` to your Django project's `INSTALLED_APPS`.

## Usage

See the IProfile [guide](https://github.com/victorfsf/python-iprofile/wiki/) and [command reference](https://github.com/victorfsf/python-iprofile/wiki/Command-Reference/) before using this.

##### Opening the shell:

```
$ python manage.py ishell <profile_name>
```

##### To open the [active IProfile](https://github.com/victorfsf/python-iprofile/wiki#activating-a-profile/), run:

```
$ python manage.py ishell .
```
