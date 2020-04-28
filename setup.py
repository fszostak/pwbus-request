#!/usr/bin/env python
from setuptools import setup, find_namespace_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name="pwbus-client",
    version="0.1.2",
    author="Fabio Szostak",
    author_email="fszostak@gmail.com",
    description="Client for PWBUS",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fszostak/pwbus-client",
    package_dir={"": "src"},
    packages=find_namespace_packages(where="src"),
    install_requires=requirements,
    setup_requires=['flake8'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7'
)
