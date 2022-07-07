from setuptools import setup, find_packages
import os

version_file_path = f'{os.path.abspath(os.path.dirname(__file__))}/src/ai21/version.py'

version_file = {}
with open(version_file_path, "rt") as f:
    exec(f.read(), version_file)
version = version_file["__version__"]

setup(
    name='ai21_studio_client',
    version='version',
    license='MIT',
    author="Amir Koblyansky",
    author_email='amirk@ai21.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[
        'requests',
    ],
)
