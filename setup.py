from setuptools import setup
setup(name='pyputio',
version='0.1.21',
description='Command Line Client for Put.io download zip archives',
url='https://github.com/jmarhee/pyputio-cli',
author='jmarhee',
author_email='jmarhee@interiorae.com',
license='MIT',
packages=['pyputio'],
python_requires='>=3.8',
entry_points = {
	'console_scripts': [
		'putio=pyputio.main:main',
		'plex-scan=pyputio.scan:main',
		'plex-empty=pyputio.empty:main',
	]
},
install_requires=[
	"progressbar",
	"requests",
	"plexapi"
],
zip_safe=False)
