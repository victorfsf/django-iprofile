# -*- coding: utf-8 -*-

from setuptools import setup
from setuptools import find_packages

version = '0.0.1'


setup(
    name='django-iprofile',
    packages=find_packages(exclude=['tests']),
    package_data={
        'iprofile_shell': [],
    },
    install_requires=[
        'python-iprofile'
    ],
    zip_safe=False,
    version=version,
    description='A Django app adapting the Django shell to work with IProfile',
    author='Victor Ferraz',
    author_email='victorfsf.dev@gmail.com',
    url='https://github.com/victorfsf/django-iprofile',
    keywords=[
        'ipython',
        'python',
        'python2',
        'python3',
        'shell',
        'profile',
        'iprofile',
        'django'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
    ],
)
