import setuptools  # type: ignore
from setuptools import setup  # type: ignore

setup(
    name="Rose",
    author="Ryu ju heon",
    author_email="SaidBySolo@gmail.com",
    url="https://github.com/SaidBySolo/Rose",
    version="4.0.0",
    packages=setuptools.find_packages(),  # type: ignore
    description="Heliotrope python wrapper",
    install_requires=["aiohttp"],
    python_requires=">=3.6",
)
