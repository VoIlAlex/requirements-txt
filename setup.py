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


class PostInstallCommand(install):
	def run(self):
		install.run(self)
		from requirements_txt.install import install as requirements_install
		requirements_install()


setup(
	# Name of the package 
	name='to-requirements.txt',
	# Packages to include into the distribution 
	packages=find_packages('.'),
	# Start with a small number and increase it with 
	# every change you make https://semver.org 
	version='1.1.7',
	# Chose a license from here: https: // 
	# help.github.com / articles / licensing - a - 
	# repository. For example: MIT 
	license='MIT',
	# Short description of your library 
	description='Automatically add and delete modules to requirements.txt installing them using pip.',
	# Long description of your library 
	long_description=long_description,
	long_description_content_type='text/markdown',
	# Your name 
	author='Ilya Vouk',
	# Your email 
	author_email='ilya.vouk@gmail.com',
	# Either the link to your github or to your website 
	url='https://github.com/VoIlAlex/russian',
	# Link from which the project can be downloaded 
	download_url='',
	# List of keywords 
	keywords=[],
	# List of packages to install with this one 
	install_requires=[
		'appdata==2.1.2',
		'click==8.0.3',
	],
	cmdclass={
		'install': PostInstallCommand,
	},
	entry_points={
		'console_scripts': [
			'requirements-txt = requirements_txt.command:cli',
		],
	},
	# https://pypi.org/classifiers/
	classifiers=[
		'Development Status :: 4 - Beta',
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
