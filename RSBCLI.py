from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
import sys
import click


class WebEnginePage(QWebEnginePage):
    def __init__(self, *args, **kwargs):
        QWebEnginePage.__init__(self, *args, **kwargs)
        self.featurePermissionRequested.connect(self.onFeaturePermissionRequested)

    def onFeaturePermissionRequested(self, url, feature):
        if feature in (QWebEnginePage.MediaAudioCapture, 
            QWebEnginePage.MediaVideoCapture, 
            QWebEnginePage.MediaAudioVideoCapture):
            self.setFeaturePermission(url, feature, QWebEnginePage.PermissionGrantedByUser)
        else:
            self.setFeaturePermission(url, feature, QWebEnginePage.PermissionDeniedByUser)


application= QApplication(sys.argv)
@click.group()
@click.version_option('0.1.4')
def main():
    """RSB - webpages in GUI VIEW"""
    pass


@main.command('open')
@click.argument('url', nargs=1)
def open(url):
    webpage = WebEnginePage()
    webengine= QWebEngineView()
    webengine.setPage(webpage)
    webengine.load(QUrl(url))
    webengine.show()

    sys.exit(application.exec_())
if __name__ == "__main__":
    main()
    
    
