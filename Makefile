
test:
	python -m unittest discover -v

lint:
	find . -path ./venv -prune -o -iname "*.py" | xargs pylint