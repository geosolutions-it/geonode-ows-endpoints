#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages

setup(
    name = "geonode-ows-endpoints",
    version = "0.1",
    description = "GeoNode OWS listing. Exposes url which lists all OWS endpoints used by layers.",
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
)


