#!/usr/bin/env python

#
# Imports
#

# System Imports
from distutils.core import setup

#
# Setup
#

setup(
    # Metadata
    name='mfgames-tools-python',
    version='0.1.0.0',
    description='A framework for object-oriented command-line utilities.',
    author='Dylan R. E. Moonfire',
    author_email="contact@mfgames.com",
    url='http://mfgames.com/mfgames-tools-python',
    classifiers=[
        "Development Status :: 1 - Planning",
        "Development Status :: 2 - Pre-Alpha",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: User Interfaces",
    ],

    # Packages
    packages=["mfgames_tools"],
    package_dir = {'': 'src'}
    )
