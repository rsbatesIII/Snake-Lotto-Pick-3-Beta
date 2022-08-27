"""
Project packaging and deployment
More details: https://setuptools.pypa.io/en/latest/userguide/quickstart.html
"""
import os
from setuptools import setup
import reporter
def __read__(file_name):
    return open(os.path.join(os.path.dirname(__file__), file_name)).read()

setup(
    name="rpm_query",
    version=__version__,
    author="Russell Bates",
    author_email="code@securewebcloud.com",
    description=__doc__,
    license="Apache",
    keywords="rpm query",
    url="https://github.com/rsbatesIII/Snake-Lotto-Pick-3-Beta",
    packages=[
        'reporter'
    ],
    long_description=__read__('README.md'),
    # https://pypi.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Games",
        "Environment :: Console",
        "Intended Audience :: Other Audience"
        "License :: Free for non-commercial use"
    ],
    setup_requires=[
        "setuptools==49.1.3",
        "wheel==0.37.0",
        "rich==9.5.1",
        "dearpygui==1.0.2"
    ],
    install_requires=[
        "rich==9.5.1",
    ],
    scripts=[
        "bin/snake_lotto.py",
    ]
)