#!/usr/bin/env python
"""
Django REST Requirements setup file.
"""
from setuptools import setup, find_packages


setup(
    name='setsuperuser',
    version='1.0.0',
    url='https://github.com/gunthercox/setsuperuser',
    description='Command to set Django super user',
    author='Gunther Cox',
    author_email='gunthercx@gmail.com',
    include_package_data=False,
    packages=find_packages(),
    package_dir={
        'setsuperuser': 'setsuperuser'
    },
    license='MIT',
    zip_safe=True,
    platforms=['any'],
    keywords=['django', 'commands'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Environment :: Web Environment',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests'
)
