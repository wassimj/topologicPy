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
    description = 'Wassim\'s Topologic module',
    url = None,
    author = 'James Bond',
    author_email = 'James.Bond.007@mi6.org',
    license = 'Spy Game License',
    packages=['topologic'],
    package_dir={'': '.'},
    data_files=[('topologic/libs', ['libTopologicCore.so'],),
        ('topologic/include', [f for f in copy_dir("./include")]),
        ('topologic/include/Utilities', [f for f in copy_dir("./include/Utilities")])
    ],
    install_requires=[
        'cppyy==1.9.1'
    ]
)
