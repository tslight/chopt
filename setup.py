# Copyright (c) 2018, Toby Slight. All rights reserved.
# ISC License (ISCL) - see LICENSE file for details.

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="chopt",
    version="0.0.6",
    author="Toby Slight",
    author_email="tobyslight@gmail.com",
    description="Choose Options using a CLI Checkbox Menu",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tslight/chopt",
    install_requires=['columns'],
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: ISC License (ISCL)",
        "Operating System :: OS Independent",
    ),
    entry_points={
        'console_scripts': [
            'chopt = chopt.__main__:main',
        ],
    }
)
