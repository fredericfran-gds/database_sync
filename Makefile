
install:
	pip install -r requirements.txt

test:
	python -m unittest discover -v

lint:
	find . -path ./venv -prune -o -iname "*.py" -print | xargs pylint
