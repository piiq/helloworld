"""My first application."""
import sys

from PySide2 import QtWidgets

from PySide2 import QtWebEngineWidgets
from PySide2.QtCore import QUrl
from PySide2.QtWebEngineWidgets import QWebEngineSettings


class HelloWorld(QtWidgets.QMainWindow):
    """Hello world."""

    def __init__(self):
        """Instantiate."""
        super(HelloWorld, self).__init__()
        self.setWindowTitle('helloworld')
        QWebEngineSettings.globalSettings().setAttribute(QWebEngineSettings.PluginsEnabled, True)
        self.centralwid = QtWidgets.QWidget(self)
        self.vlayout = QtWidgets.QVBoxLayout()
        self.webview = QtWebEngineWidgets.QWebEngineView()
        self.webview.setUrl(QUrl("https://www.youtube.com/watch?v=dQw4w9WgXcQ"))
        self.vlayout.addWidget(self.webview)
        self.centralwid.setLayout(self.vlayout)
        self.setCentralWidget(self.centralwid)
        self.show()


def main():
    """Run forever."""
    app = QtWidgets.QApplication(sys.argv)
    main_window = HelloWorld()
    main_window.resize(720, 480)
    sys.exit(app.exec_())
