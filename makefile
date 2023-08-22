
build: 
	python setup.py .

tests:
	export PYTHONPATH=. && pytest test\

