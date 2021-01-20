from setuptools import setup, Extension
import os
def copy_dir(dir_path):
    base_dir = os.path.join('topologic', dir_path)
    for (dirpath, dirnames, files) in os.walk(base_dir):
        for f in files:
            yield os.path.join(dirpath.split('/', 1)[1], f)
setup(
    name = 'topologic',
    version = '0.2',
    description = 'Topologic for Linux and Python 3.8',
    url = None,
    author = 'Wassim Jabi',
    author_email = 'wassim.jabi@gmail.com',
    license = 'AGPL',
    packages=['topologic'],
    package_dir={'': '.'},
    data_files=[
        ('topologic/include', [f for f in copy_dir("./include")]),
        ('topologic/include/Utilities', [f for f in copy_dir("./include/Utilities")])
    ],
    install_requires=[
        'cppyy==1.3.0'
    ]
)
