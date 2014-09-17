# -*- coding: utf-8 -*-
from __future__ import with_statement
from setuptools import setup
from urwid_stackedwidget import __version__

setup(
    name='urwid-stackedwidget',
    version=__version__,
    license='MIT',
    author='Sumin Byeon',
    author_email='suminb@gmail.com',
    maintainer='',
    url='https://github.com/suminb/urwid-stackedwidget',
    description='A widget container that presents one child widget at a time.',
    long_description=__doc__,
    platforms='any',
    py_modules=['urwid_stackedwidget'],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: Public Domain',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries :: Python Modules'],
    install_requires=['urwid'],
)
