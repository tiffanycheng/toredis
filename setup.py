#!/usr/bin/env python
"""
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from distutils.core import setup

import sys

major, minor = sys.version_info[:2]

kwargs = {}

if major >= 3:
    import setuptools  # setuptools is required for use_2to3
    kwargs["use_2to3"] = True

setup(
    name='toredis',
    version='0.1.1',
    description='Really simple async Redis client for Tornado',
    author='Josh Marshall',
    author_email='catchjosh@gmail.com',
    url = "http://github.com/joshmarshall/toredis/",
    license = "http://www.apache.org/licenses/LICENSE-2.0",
    packages=['toredis',],
    package_data={'toredis': ['commands.json']},
    install_requires=['tornado',],
    **kwargs
)
