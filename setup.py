#!/usr/bin/env python

"""
Asyncio gunicorn worker with websockets support.
"""
from setuptools import setup


setup(
    name='gaiohttp-websocket',
    version='0.1',
    url='https://github.com/urbaniak/gaiohttp-websocket',
    license='BSD',
    author='Krzysztof Urbaniak',
    author_email='urban@fail.pl',
    description='Asyncio websockets for gunicorn.',
    long_description=__doc__,
    py_modules=['gaiohttp_websocket'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'gunicorn',
        'aiohttp',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ]
)
