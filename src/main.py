from PySide6 import QtGui, QtWidgets
from PySide6.QtWidgets import QFileDialog


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("NovaCode")
        self.resize(800, 600)

        # Zentrales Textfeld
        self.editor = QtWidgets.QPlainTextEdit()
        self.setCentralWidget(self.editor)

        # Aktuell geöffnete Datei
        self.current_file = None

        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")

        open_action = QtGui.QAction("Open", self)
        save_action = QtGui.QAction("Save", self)
        save_as_action = QtGui.QAction("Save As", self)
        exit_action = QtGui.QAction("Exit", self)
        open_action.setShortcut("Ctrl+O")
        save_action.setShortcut("Ctrl+S")
        save_as_action.setShortcut("Ctrl+Shift+S")
        exit_action.setShortcut("Ctrl+Q")

        open_action.triggered.connect(self.open_file)
        save_action.triggered.connect(self.save_file)
        save_as_action.triggered.connect(self.save_as_file)
        exit_action.triggered.connect(self.close)

        file_menu.addAction(open_action)
        file_menu.addAction(save_action)
        file_menu.addAction(save_as_action)
        file_menu.addSeparator()
        file_menu.addAction(exit_action)

    def open_file(self):
        path, _ = QFileDialog.getOpenFileName(self, "Open File")
        if path:
            with open(path, "r", encoding="utf-8") as file:
                self.editor.setPlainText(file.read())
            self.current_file = path
            self.setWindowTitle(f"NovaCode - {path}")

    def save_file(self):
        if self.current_file:
            with open(self.current_file, "w", encoding="utf-8") as file:
                file.write(self.editor.toPlainText())
        else:
            self.save_as_file()

    def save_as_file(self):
        path, _ = QFileDialog.getSaveFileName(self, "Save File As")
        if path:
            with open(path, "w", encoding="utf-8") as file:
                file.write(self.editor.toPlainText())
            self.current_file = path
            self.setWindowTitle(f"NovaCode - {path}")


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    ui = MainWindow()
    ui.show()
    app.exec()
