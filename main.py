from PyQt5.QtWidgets import QApplication, QDialog, QLineEdit, QPushButton
from maindlg import MainDlg
from qt_material import apply_stylesheet
import sys
def main():

    app = QApplication(sys.argv)
    mainDlg = MainDlg()
    apply_stylesheet(app, theme='dark_teal.xml')
    # mainDlg.showFullScreen()
    mainDlg.show()
    sys.exit(app.exec_())
    

if __name__ == "__main__":
    main()

