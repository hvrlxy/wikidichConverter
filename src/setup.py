from setuptools import setup, find_packages

setup(
    name='wikidichConverter',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT License',
    description="Python Package that convert wikidich books to PDF files",
    long_description=open('README.md').read(),
    install_requires=[],
    url='https://github.com/hvrlxy/wikidichConverter',
    author='Ha Le',
    author_email='le.ha1@northeastern.edu',
    setup_requires=['setuptools_scm'],
    include_package_data=True
)