#!/usr/bin/env python3

import os
import sys


try:
    from setuptools import setup
except:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist bdist_wheel upload')
    sys.exit()

setup(
    name='kl',
    version='4.0.0',
    description='Simple keylogger for Linux + X11',
    author='Cristian Cabrera',
    author_email='surrealcristian@gmail.com',
    url='https://github.com/surrealists/kl',
    keywords='keylogger linux x11',
    license='MIT',
    py_modules = ['kl'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: X11 Applications',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries',
        'Topic :: System :: Monitoring',
        'Topic :: Utilities',
    ],
)
