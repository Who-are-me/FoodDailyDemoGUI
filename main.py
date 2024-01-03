import sys

from src.window import Widget
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QFile


# main function
if __name__ == "__main__":
    # load style from file
    style_sheet = QFile('src/resource/Yashi.qss')
    style_sheet.open(QFile.OpenModeFlag.ReadOnly)
    convert = style_sheet.readAll().toStdString()

    app = QApplication(sys.argv)
    # load style to App
    app.setStyleSheet(convert)

    widget = Widget()
    widget.show()
    sys.exit(app.exec())
