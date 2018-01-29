.PHONY: run install upgrade designer uic

PYTHON=python3
PYUIC=$(PYTHON) -m PyQt5.uic.pyuic

SRC=main.py  main_window.py  money_document.py  money_document_ui.py

run: $(SRC)
	$(PYTHON) main.py

designer:
	designer

install:
	pip install -U -r requirements-devel.txt
	#conda install sqlalchemy

upgrade:
	conda update --all

touch:
	touch ui/*.ui

money_document_ui.py: ui/money-document.ui
	$(PYUIC) $< > $@

main_window.py: ui/main-window.ui
	$(PYUIC) $< > $@
