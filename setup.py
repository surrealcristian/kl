#!/usr/bin/env python

import os
import sys

try:
    from setuptools import setup
except:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

packages = ['kl']
requires = []

setup(
    name='kl',
    version='1.0.2',
    description='Simple keylogger for Linux + X11',
    author='Cristian Cabrera',
    author_email='surrealcristian@gmail.com',
    url='https://github.com/surrealists/kl',
    packages=packages,
    package_dir={'kl': 'kl'},
    include_package_data=True,
    install_requires=requires,
    license='MIT',
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: X11 Applications',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries',
        'Topic :: System :: Monitoring',
        'Topic :: Utilities',
    ],
)
