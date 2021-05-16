import setuptools  # type: ignore
from setuptools import setup  # type: ignore

requirements = []
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Peppermint",
    author="Ryu ju heon",
    author_email="SaidBySolo@gmail.com",
    url="https://github.com/SaidBySolo/Peppermint",
    version="4.0.0",
    long_description=open("README.md", "rt", encoding="UTF8").read(),
    packages=setuptools.find_packages(),  # type: ignore
    description="Heliotrope python wrapper",
    install_requires=requirements,
    python_requires=">=3.6",
)
