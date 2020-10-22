from setuptools import setup
setup(name='pyputio',
version='0.1.11',
description='Command Line Client for Put.io download zip archives',
url='https://git-central.openfunction.co/jmarhee/pyputio-cli',
author='jmarhee',
author_email='jmarhee@interiorae.com',
license='MIT',
packages=['pyputio'],
python_requires='>=3.8',
entry_points = {
	'console_scripts': ['putio=pyputio.main:main']
},
install_requires=[
],
zip_safe=False)
