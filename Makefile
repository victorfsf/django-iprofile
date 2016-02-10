clean:
	@find . -name '*.pyc' -exec rm -f {} \;
	@find . -name 'Thumbs.db' -exec rm -f {} \;
	@find . -name '*~' -exec rm -f {} \;
	@find . -name '*.pyc' -exec rm -f {} \;
	@find . -name '__pycache__' -exec rm -fr {} \;

requirements:
	@pip install -r requirements.txt

setup: clean requirements

dist:
	@python setup.py sdist
	@python setup.py bdist_wheel --universal

register:
	@twine register dist/*.tar.gz
	@twine register dist/*.whl

upload:
	@twine upload dist/*

pypi: dist register upload
