dist:
	python setup.py bdist_wheel

push-test:
	python3 -m twine upload --repository testpypi dist/*	

push:
	python3 -m twine upload dist/*

install:
	pip3 install -e .

