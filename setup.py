# -*- coding: utf-8 -*-

"""
Setup file for Tetris.
"""

from setuptools import setup

setup(
    name="Tetris",
    version="0.1.0",
    author="Marcus Veibäck",
    author_email="sirmar@gmail.com",

    packages=["tetris"],
    include_package_data=True,
    url="https://github.com/sirmar/tetris",

    license="LICENSE",
    description="Yes another Tetris.",
    long_description=open("README.org").read(),

    entry_points={
        'console_scripts': [
            'tetris=tetris.main:main',
        ]
    },

    install_requires=[
        "nose",
        "coverage",
        "mock",
        "pylint"
    ])
