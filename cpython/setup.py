'''
// This file is part of Topologic software library.
// Copyright(C) 2019, Cardiff University and University College London
//
// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU Affero General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
// GNU Affero General Public License for more details.
//
// You should have received a copy of the GNU Affero General Public License
// along with this program. If not, see <https://www.gnu.org/licenses/>.
'''
from setuptools import setup, Extension
import os
def copy_dir(dir_path):
    base_dir = os.path.join('topologic', dir_path)
    for (dirpath, dirnames, files) in os.walk(base_dir):
        for f in files:
            print (f)
            yield os.path.join(dirpath.split('/', 1)[1], f)
setup(
    name = 'topologic',
    version = '0.3',
    description = 'Topologic for Linux and Python 3.8',
    url = None,
    author = 'Wassim Jabi',
    author_email = 'wassim.jabi@gmail.com',
    license = 'AGPL',
    packages=['topologic'],
    package_dir={'': '.'},
    install_requires=[
        'cppyy>=1.3.0'
    ]
)
