#!/usr/bin/env python3
# encoding: utf-8

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('{{ cookiecutter.project_slug }}/metadata.py') as metadata_file:
    exec(metadata_file.read())

with open('README.rst') as readme_file:
    readme = readme_file.read()

requirements = [
        'kxg',
]

test_requirements = [
]


setup(
    name='{{ cookiecutter.project_slug }}',
    version=__version__,
    author=__author__,
    author_email=__email__,
    long_description=readme,
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}',
    packages=[
        '{{ cookiecutter.project_slug }}',
    ],
    entry_points = {
        'console_scripts': [
            '{{ cookiecutter.project_slug }}={{ cookiecutter.project_slug }}:main',
        ],
    },
    include_package_data=True,
    install_requires=requirements,
    license='GPLv3',
    zip_safe=False,
    keywords=[
        '{{ cookiecutter.project_slug }}',
        'game',
    ],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Games/Entertainment',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
