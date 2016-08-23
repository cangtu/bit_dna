# -*- coding: utf-8 -*-
#
# Copyright @ Pylego.
#
# 16-8-23 3:59PM jaglawz@gmail.com
#
# Distributed under terms of the MIT License
from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(
    name='bit_dna',
    author='Pylego',
    author_email='jaglawz@gmail.com',
    license='MIT',
    version='1.0.0',
    description='transform DNA sequence to binary format, read correspond binary string to DNA sequence',
    url='https://github.com/pylego/bit_dna',
    long_description=readme(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Topic :: Scientific/Engineering :: Bio-Informatics'
    ],
    zip_safe=False,
)
