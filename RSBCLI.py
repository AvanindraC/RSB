from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
import sys
import click

urls = {
    'github': "https://github.com/" ,
    'youtube': "https://youtube.com",
    'discord': "https://discord.com/",
    'pypi': "https://pypi.org" ,
    'stackoverflow': "https://stackoverflow.com",
    'AISC': "https://aistudent.community/",
    'reddit': "https://reddit.com",
    'gmail': "https://www.gmail.com/",
    'spotify': "https://spotify.com",
    'udemy': "https://www.udemy.com",
    'linuxmint': "https://linuxmint.com/",
    'dogemeet': "https://doge-meet-demo.up.railway.app/"
}


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
def _downloadRequested(item): # QWebEngineDownloadItem
    print('downloading to', item.path())
    item.accept()



application= QApplication(sys.argv)

@click.group()
@click.version_option('0.2.5')
def main():
    """RSB - webpages in GUI VIEW"""
    pass



@main.command('open', help= '"rsb open <url>" opens your desired URL in RSB window' )
@click.argument('url', nargs=1)
def open(url):
    
    webpage = WebEnginePage()
    webengine= QWebEngineView()
    webengine.setWindowTitle("R S B")
    webengine.page().profile().downloadRequested.connect(_downloadRequested)   
    webengine.setPage(webpage)
    webengine.load(QUrl(url))
    webengine.show()



    sys.exit(application.exec_())

@main.command('open_pre', help = "Allows you to use presets for websites. See the presets using the 'presets' command. Syntax : 'rsb open_pre '")
@click.argument('i', nargs = 1)
def open_pre(i):
    webpage = WebEnginePage()
    webengine= QWebEngineView()
    webengine.setWindowTitle("R S B")
    webengine.page().profile().downloadRequested.connect(_downloadRequested)   
    webengine.setPage(webpage)
    url = urls[i]
    webengine.load(QUrl(url))
    webengine.show()
    sys.exit(application.exec_())
@main.command('presets', help = 'type "presets" to get a list of preset websites. Syntax to run presets: "rsb open urls[enter the index]"')
def presets():
    for key, item in urls.items():
        print(f"{key} {item}")
if __name__ == "__main__":
    main()
