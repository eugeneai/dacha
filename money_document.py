from PyQt5.QtWidgets import QDialog
from money_document_ui import Ui_Dialog

class MoneyDocumentController:
    def __init__(self, view):
        self.context=view
        self.view=view
        ui = view.ui
        ui.spinBox.valueChanged[int].connect(self.on_spinbox_value_changed)

    def on_spinbox_value_changed(self, value):
        self.view.model.amount=float(value)

class MoneyDocumentView(QDialog):

    def get_model(self):
        return self.context

    model = property(get_model)

    def __init__(self, doc):
        super(MoneyDocumentView, self).__init__()
        self.context=doc
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)
        self.controller=MoneyDocumentController(self)
        self.update()

    def update(self):
        self.ui.spinBox.setProperty("value", self.context.amount)

