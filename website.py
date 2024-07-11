import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QMainWindow, QApplication, QStatusBar, QToolBar, QAction

class WebBrowser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://www.google.com'))
        self.browser.urlChanged.connect(self.update_AddressBar)
        self.setCentralWidget(self.browser)

        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)

        self.navigation_bar = QToolBar('Navigation Toolbar')
        self.addToolBar(self.navigation_bar)

        back_button = QAction("Back", self)
        back_button.setStatusTip('Go to the previous page')
        back_button.triggered.connect(self.browser.back)
        self.navigation_bar.addAction(back_button)

        refresh_button = QAction("Refresh", self)
        refresh_button.setStatusTip('Refresh this page')
        refresh_button.triggered.connect(self.browser.reload)
        self.navigation_bar.addAction(refresh_button)

        forward_button = QAction("forward", self)
        forward_button.setStatusTip('forward this page')
        forward_button.triggered.connect(self.browser.forward)
        self.navigation_bar.addAction(forward_button)

    def update_AddressBar(self, url):
        self.status_bar.showMessage(url.toString())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WebBrowser()
    window.show()
    sys.exit(app.exec_())
