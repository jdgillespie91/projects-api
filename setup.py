import os
import re
from setuptools import setup, find_packages

setup(
    name='projects',
    version='0.1.0',
    packages=find_packages(exclude=['tests']),
    description='A JSON api describing my personal projects.',
    author='Jake Gillespie',
    author_email='jdgillepsie91@gmail.com',
    zip_safe=True,
    classifiers=[
        "Private :: Don't upload",
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    install_requires=[
        'falcon',
        'gunicorn',
    ],
)
