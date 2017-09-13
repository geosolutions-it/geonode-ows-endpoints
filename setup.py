#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages

def readme():
    with open(os.path.join(os.path.dirname(__file__), 'README.txt')) as f:
        return f.read()

setup(
    name = "geonode-ows-endpoints",
    version = "0.2",
    description = "GeoNode OWS listing. Exposes url which lists all OWS endpoints used by layers.",
    long_description = readme(),
    url = 'https://github.com/geosolutions-it/geonode-ows-endpoints',
    author = "Cezary Statkiewicz",
    author_email = 'cezary.statkiewicz@geo-solutions.it',
    keywords = ['geonode', 'monitoring', 'geohealthcheck', 'integration api', 'gis'],
    packages =['geonode_ows_endpoints'],
    package_dir = {'geonode_ows_endpoints': os.path.join(*('src/geonode_ows_endpoints/').split('/')),
                   '': 'src'},
    include_package_data = True,
    zip_safe = False,
    install_requires=[
        'GeoNode<2.7',
    ],
    classifiers = ['Development Status :: 4 - Beta',
                   'Environment :: Web Environment',
                   'Environment :: Plugins',
                   'Framework :: Django',
                   'Intended Audience :: System Administrators',
                   'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
                   'Topic :: Scientific/Engineering :: GIS'
                   ]
)


