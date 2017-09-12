# sample ./setup.py file
from setuptools import setup

setup(
    name="onaji",
    packages = ['onaji'],
    version = "0.1.0",
    scripts = ['bin/onajidiff'],

    # the following makes a plugin available to pytest
    entry_points = {
        'pytest11': [
            'onaji = onaji.logger',
        ],
    },

    # custom PyPI classifier for pytest plugins
    classifiers=[
        "Framework :: Pytest",
    ],
)