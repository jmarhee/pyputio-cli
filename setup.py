from setuptools import setup
setup(name='pyputio',
version='0.1.4',
description='Command Line Client for Put.io download zip archives',
url='https://github.com/jmarhee/pyputio-cli',
author='jmarhee',
author_email='jmarhee@interiorae.com',
license='MIT',
packages=['pyputio'],
entry_points = {
	'console_scripts': ['putio=pyputio.main:main']
},
install_requires=[
],
zip_safe=False)
