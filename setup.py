#!/usr/bin/env python
from setuptools import setup, find_packages
import pathlib
import pkg_resources
# import versioneer


with pathlib.Path('requirements.txt').open() as requirements_txt:
    install_requires = [
        str(requirement)
        for requirement
        in pkg_resources.parse_requirements(requirements_txt)
    ]

with pathlib.Path('requirements_test.txt').open() as requirements_txt:
    test_install_requires = [
        str(requirement)
        for requirement
        in pkg_resources.parse_requirements(requirements_txt)
    ]

setup(name='examplepackage',
      description='An example package',
      author='Jacob Marlow',
      author_email='',
      url='',
      # version=versioneer.get_version(),
      packages=find_packages(),
      entry_points='''
        [console_scripts]
        hello=example_main:hello
      ''',
      install_requires=install_requires,
      extras_require={'test': test_install_requires}
      )
