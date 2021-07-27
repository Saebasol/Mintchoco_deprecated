import setuptools  # type: ignore
from setuptools import setup  # type: ignore

import mintchoco

setup(
    name="mintchoco",
    author="Ryu ju heon",
    author_email="SaidBySolo@gmail.com",
    url="https://github.com/SaidBySolo/Mintchoco",
    version=mintchoco.__version__,
    long_description=open("README.md", "rt", encoding="UTF8").read(),
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),  # type: ignore
    description="Heliotrope python wrapper",
    python_requires=">=3.9",
)
