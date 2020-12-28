from setuptools import setup, Extension

setup(
    name = 'topologic',
    version = '0.1',
    description = 'Wassim\'s Topologic module',
    url = None,
    author = 'James Bond',
    author_email = 'James.Bond.007@mi6.org',
    license = 'Spy Game License',
    packages=['topologic'],
    package_dir={'': '.'},
    package_data={'./topologic/': ['libTopologicCore.so']},
)
