from setuptools import setup, find_namespace_packages

import os
cdir = os.path.dirname(os.path.realpath(__file__))

setup(
    name="PyUnikeyNT",
    version="1.0",
    author="Vic P.",
    author_email="vic4key@gmail.com",
    packages=find_namespace_packages(exclude=["tests"]),
    url="https://github.com/vic4key/PyUnikeyNT.git",
    license="LICENSE",
    description="Unikey NT with Python",
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    install_requires=[],
    include_package_data=True,
    package_data={
        "PyUnikeyNT.x64": [os.path.join(cdir, R"PyUnikeyNT\x64\PyUnikeyNT.dll")],
        "PyUnikeyNT.Win32": [os.path.join(cdir, R"PyUnikeyNT\Win32\PyUnikeyNT.dll")],
    },
)