import setuptools
from setuptools import setup

setup(
    name="Rose",
    author="Ryu ju heon",
    author_email="SaidBySolo@gmail.com",
    url="https://github.com/SaidBySolo/Rose",
    version="1.4.0",
    packages=setuptools.find_packages(),
    description="Heliotrope python wrapper",
    install_requires=["aiohttp"],
    python_requires=">=3.6",
)
