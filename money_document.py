from PyQt5.QtWidgets import QDialog
from money_document_ui import Ui_Dialog

class MoneyDocumentDialog(QDialog):
    def __init__(self):
        super(MoneyDocumentDialog, self).__init__()
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)
