#!/usr/bin/env python3

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
#with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
#	long_description = f.read()

setup(
	name='Xie',

	# Versions should comply with PEP440.  For a discussion on single-sourcing
	# the version across setup.py and the project code, see
	# https://packaging.python.org/en/latest/single_source_version.html
	version='0.0.3',

	description='試圖以筆劃描述漢字的函式庫',
#	long_description=long_description,
	long_description='試圖以筆劃描述漢字的函式庫',

	# The project's main homepage.
	url='https://github.com/xrloong/Xie',

	# Author details
	author='xrloong',
	author_email='xrloong@gmail.com',

	# Choose your license
	license='Apache',

	# See https://pypi.python.org/pypi?%3Aaction=list_classifiers
	classifiers=[
		# How mature is this project? Common values are
		#   3 - Alpha
		#   4 - Beta
		#   5 - Production/Stable
		'Development Status :: 3 - Alpha',

		# Indicate who your project is intended for
		'Intended Audience :: Developers',
		'Topic :: Software Development :: Build Tools',

		# Pick your license as you wish (should match "license" above)
		'License :: OSI Approved :: Apache Software License',

		'Programming Language :: Python :: 3 :: Only',
	],

	# What does your project relate to?
	keywords='qiangheng',

	packages=find_packages(exclude=['contrib', 'docs', 'tests*']),


	# List run-time dependencies here.  These will be installed by pip when
	# your project is installed. For an analysis of "install_requires" vs pip's
	# requirements files see:
	# https://packaging.python.org/en/latest/requirements.html
	install_requires=[],

	# To provide executable scripts, use entry points in preference to the
	# "scripts" keyword. Entry points provide cross-platform support and allow
	# pip to create the appropriate form of executable for the target platform.
	entry_points={
		'console_scripts': [
			'xie=xie:xie',
		],
	},
)
