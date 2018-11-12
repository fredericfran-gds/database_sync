
install:
	pip install -r requirements.txt
	pip install pylint==1.9.3

test:
	python -m unittest discover -v

lint:
	find . -path ./venv -prune -o -iname "*.py" | xargs pylint
