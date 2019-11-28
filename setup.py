#!/usr/bin/env python
import os
from setuptools import setup, find_packages


def read(fname):
    """Open files relative to package."""
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def find_scripts():
    """Find Python script files."""
    scripts = []
    exclude = ['setup.py']
    for file in os.scandir('.'):
        if file.name.endswith('.py') and file.is_file() and (file.name not in exclude):
            scripts.append(file.name)
    return scripts


setup(
    name='pipp',
    version='0.1.0',
    author="Thomas Bouve (@crahan)",
    author_email="crahan@n00.be",
    description='Python pip wrapper script.',
    long_description=read('README.md'),
    long_description_content_type="text/markdown",
    license='MIT',
    packages=find_packages(),
    scripts=find_scripts(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
    ],
    install_requires=[
        'yamjam',
    ],
)
