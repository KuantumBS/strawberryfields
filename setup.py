# Copyright 2019 Xanadu Quantum Technologies Inc.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import os
import sys

from setuptools import setup


with open("strawberryfields/_version.py") as f:
    version = f.readlines()[-1].split()[-1].strip("\"'")


requirements = [
    "numpy>=1.16.3",
    "scipy>=1.0.0",
    "networkx>=2.0",
    "quantum-blackbird>=0.2.0",
    "thewalrus>=0.10",
    "toml",
    "appdirs",
]

info = {
    "name": "StrawberryFields",
    "version": version,
    "maintainer": "Xanadu Inc.",
    "maintainer_email": "software@xanadu.ai",
    "url": "https://github.com/XanaduAI/StrawberryFields",
    "license": "Apache License 2.0",
    "packages": [
        "strawberryfields",
        "strawberryfields.circuitspecs",
        "strawberryfields.gbs",
        "strawberryfields.backends",
        "strawberryfields.backends.tfbackend",
        "strawberryfields.backends.fockbackend",
        "strawberryfields.backends.gaussianbackend",
    ],
    "package_data": {"strawberryfields": ["backends/data/*", "gbs/data/*"]},
    "include_package_data": True,
    "description": "Open source library for continuous-variable quantum computation",
    "long_description": open("README.rst", encoding="utf-8").read(),
    "provides": ["strawberryfields"],
    "install_requires": requirements,
    # 'extras_require': extra_requirements,
    "command_options": {
        "build_sphinx": {"version": ("setup.py", version), "release": ("setup.py", version)}
    },
}

classifiers = [
    "Development Status :: 4 - Beta",
    "Environment :: Console",
    "Intended Audience :: Science/Research",
    "License :: OSI Approved :: Apache Software License",
    "Natural Language :: English",
    "Operating System :: POSIX",
    "Operating System :: MacOS :: MacOS X",
    "Operating System :: POSIX :: Linux",
    "Operating System :: Microsoft :: Windows",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3 :: Only",
    "Topic :: Scientific/Engineering :: Physics",
]

setup(classifiers=classifiers, **(info))
