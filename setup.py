#!/usr/bin/env python3
from setuptools import setup, find_packages

__version__ = "0.0.1"
setup(
    name="ros_command",
    version=__version__,
    keywords=["ros"],
    description="ros command",
    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=[],
    scripts=["bin/rosbuild"]
)

