.PHONY: run install upgrade designer uic tests

ENV=/home/stud/.pyenv/versions/dacha/bin

PYTHON=$(ENV)/python -u
NOSE=$(ENV)/nosetests
PYUIC=$(PYTHON) -m PyQt5.uic.pyuic -x

SRC=main.py  main_window.py  money_document.py  money_document_ui.py

run: $(SRC)
	$(PYTHON) main.py

tests:
	$(NOSE) -s .

designer:
	designer

install:
	pip install -U -r requirements-devel.txt
	#conda install sqlalchemy

upgrade:
	pip install -U
	#conda update --all

touch:
	touch ui/*.ui

money_document_ui.py: ui/money-document.ui
	$(PYUIC) $< -o $@

main_window.py: ui/main-window.ui
	$(PYUIC) $< -o $@
