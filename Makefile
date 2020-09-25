dist:
	rm -rf dist/ ; python3 setup.py bdist_wheel --universal

.SILENT:
tag-release:
	if [[ $(TAG) == v?.?.? ]]; then echo "Tagging $(TAG)"; else echo "Bad Tag Format: $(TAG)"; exit 1; fi && git tag -a $(TAG) -m "Releasing $(TAG)" ; read -p "Push tag: $(TAG)? " push_tag ; if ["$push_tag"=="yes"]; then git push origin $(TAG); fi

push-test:
	make dist; python3 -m twine upload --repository testpypi dist/*	

push:
	make dist; python3 -m twine upload dist/*

install:
	pip3 install -e .

