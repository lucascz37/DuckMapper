from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="DuckMapper",
    version="1.0.1",
    author="Lucas A. Andrade",
    author_email="luke.andrade99@gmail.com",
    packages=["DuckMapper"],
    description="A tiny library to help you to convert classes to DTO and vice versa.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lucascz37/DuckMapper",
    license="MIT",
    keywords="DTO conversor mapper classMapper DuckMapper",
)
