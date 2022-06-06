import sys

from setuptools import setup, find_packages


py_version = sys.version_info[:2]
if py_version[0] < 3 and py_version not in [(2, 6), (2, 7)]:
    raise RuntimeError("Python 2.6 and up is required")


setup(
    name="moriarty",
    version='1.0.0',
    author="",
    author_email="",
    description="Client library for finding important information about a spesific phone number.",
    url="",
    license="",
    classifiers=[
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ],
    install_requires=[
        'selenium',
        'phonenumbers',
        'pyvirtualdisplay',
        'requests',
        'undetected_chromedriver',
        'clint',
        'certifi',
        'bs4',
    ],
    packages=find_packages(include=['moriarty_lib', 'moriarty_lib.*']),
)
