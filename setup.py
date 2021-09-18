#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: DeepDialog
# Mail: thebotbot@sina.com
# Created Time: 2020-01-01
#############################################

import os
from setuptools import setup, find_packages

current_dir = os.path.realpath(os.path.dirname(__file__))

ON_RTD = os.environ.get('READTHEDOCS') == 'True'
if not ON_RTD:
    INSTALL_REQUIRES = open(os.path.join(
        current_dir,
        'requirements.txt'
    )).read().split('\n')
else:
    INSTALL_REQUIRES = []

VERSION = os.path.join(
    current_dir,
    'object_detect',
    'version.txt'
)

setup(
    name='object_detect',
    version=open(VERSION, 'r').read().strip(),
    keywords=('cv', 'onnx'),
    description='Object Detect',
    long_description='Object Detect',
    license='Private',
    url='https://github.com/deepdialog/ObjectDetect',
    author='deepdialog',
    author_email='mail@qhduan.com',
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    install_requires=INSTALL_REQUIRES
)
