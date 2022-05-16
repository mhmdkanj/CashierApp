import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="cashier",
    version="0.0.1",
    description="CashierApp for receipt generation",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Mohamad Kanj",
    author_email="mhmd.kanj@gmail.com",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(exclude=("tests",)),
    include_package_data=True,
    install_requires=[],
    python_requires='>=3.7.0',
    tests_require=[
        'pytest',
        'pytest-mock'
    ],
    entry_points={
        "console_scripts": [
            "cashier=cashier.__main__:main",
        ]
    }
)
