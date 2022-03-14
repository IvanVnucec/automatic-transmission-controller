"""Python setup.py for automatic_transmission_controller package"""
import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("automatic_transmission_controller", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="automatic_transmission_controller",
    version=read("automatic_transmission_controller", "VERSION"),
    description="Awesome automatic_transmission_controller created by IvanVnucec",
    url="https://github.com/IvanVnucec/automatic-transmission-controller/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="IvanVnucec",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["automatic_transmission_controller = automatic_transmission_controller.__main__:main"]
    },
    extras_require={"test": read_requirements("requirements-test.txt")},
)
