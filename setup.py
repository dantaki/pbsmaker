from setuptools import setup
setup(
	name='pbsmaker',
	version='0.0.4',
	url='https://github.com/dantaki/pbsmaker',
	author='Danny Antaki',
	author_email='dantaki@ucsd.edu',
	packages=['pbsmaker'],
	package_dir={'pbsmaker': 'pbsmaker/'},
	include_package_data=True,
	scripts= ['pbsmaker/pbsmaker']
)
