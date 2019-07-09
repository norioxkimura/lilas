
help:
	@:

clean: distclean ;

distclean:
	rm -rf "$$(readlink -f python-venv)"
	git clean -xdf .

install: _python-venv
	./python-venv/bin/pip install -e '.[dev]'

build: _python-venv
	./python-venv/bin/python setup.py bdist_wheel

format: _python-venv
	./format $(O)

lint: _python-venv
	./lint $(O)

_python-venv python-venv:
	ln -sfT "$$(mktemp -d)" python-venv
	python3 -m venv "$$(readlink -f python-venv)"
	./python-venv/bin/pip install -U pip setuptools wheel
	touch _python-venv

SHELL = /bin/bash

.PHONY: help clean distclean install build format lint
