from setuptools import setup, find_packages

setup(
    name="gdstarter",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "inquirer",
        "requests"
    ],
    entry_points={
        "console_scripts": [
            "gdstarter = gdstarter.main:main",
        ],
    },
)
