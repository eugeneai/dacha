.PHONY: run

SRC=main.py  main_window.py  money_document.py  money_document_ui.py

run: $(SRC)
	python main.py

money_document_ui.py: ui/money-document.ui
	pyuic5 $< > $@

main_window.py: ui/main-window.ui
	pyuic5 $< > $@
