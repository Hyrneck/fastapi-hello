# setup.py
from setuptools import setup, find_packages

setup(
    name="fastapi_hello",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "uvicorn",
        "mangum"
    ],
    description="A minimal FastAPI hello world application.",
    author="Anthony Shea",
    author_email="agshea25gmail.com",
)

