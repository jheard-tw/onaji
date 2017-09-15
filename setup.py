# sample ./setup.py file
from setuptools import setup

setup(
    name="onaji",
    description="A tool for creating regression tests through logging data during pytest runs.",
    url="https://github.com/teamworksapp/onaji",
    author="Jefferson Heard",
    author_email="jheard@teamworks.com",
    license = "MIT",
    packages = ['onaji'],
    version = "0.1.1",
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
        "Development Status :: 3 - Alpha",
        "Topic :: Software Development :: Build Tools",
        "Programming Language :: Python :: 3",
    ],

    install_requires=["dulwich"],
    python_requires='>=3'
)
