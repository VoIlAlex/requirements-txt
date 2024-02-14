from distutils.core import setup
import os
from setuptools import find_packages
from setuptools.command.install import install

# User-friendly description from README.md
current_directory = os.path.dirname(os.path.abspath(__file__))
try:
	with open(os.path.join(current_directory, 'README.md'), encoding='utf-8') as f:
		long_description = f.read()
except Exception:
	long_description = ''


setup(
	# Name of the package 
	name='test_package',
	# Packages to include into the distribution 
	packages=find_packages('.'),
	# Start with a small number and increase it with 
	# every change you make https://semver.org 
	version='0.0.1',
	# Chose a license from here: https: // 
	# help.github.com / articles / licensing - a - 
	# repository. For example: MIT 
	license='MIT',
	# Short description of your library 
	description='Test package',
	# Long description of your library 
	long_description=long_description,
	long_description_content_type='text/markdown',
	# Your name 
	author='Ilya Vouk',
	# Your email 
	author_email='ilya.vouk@gmail.com',
	# List of keywords 
	keywords=[
		'test',
		'package',
	],
	# List of packages to install with this one 
	install_requires=[
	],
	# https://pypi.org/classifiers/
	classifiers=[
		'Development Status :: 5 - Production/Stable',
		'Environment :: Console',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Operating System :: Unix',
		'Topic :: Software Development',
		'Topic :: System :: Installation/Setup',
		'Topic :: Terminals',
		'Topic :: Utilities',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
		'Programming Language :: Python :: 3.8',
		'Programming Language :: Python :: 3.9',
		'Programming Language :: Python :: 3.10',
	]
)
