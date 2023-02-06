import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile, QThread, Slot
from ui_form import Ui_Widget
import time
from pySmartDL import SmartDL
from PySide6.QtCore import QThread, Signal, Slot

class DownloadThread(QThread):
    progress_signal = Signal(str)

    def __init__(self, url, parent=None):
        super().__init__(parent)
        self.url = url

    @Slot()
    def run(self):
        #obj = SmartDL(self.url, progress_bar=False)
        obj = SmartDL(self.url, dest='C:/Users/Boltiana SP/Downloads', progress_bar=False)
        obj.start(blocking=False)
        while not obj.isFinished():
            status = "Speed: %s\n" % obj.get_speed(human=True) + \
                     "Already downloaded: %s\n" % obj.get_dl_size(human=True) + \
                     "Eta: %s\n" % obj.get_eta(human=True) + \
                     "Progress: %d%%\n" % (obj.get_progress()*100) + \
                     "Progress bar: %s\n" % obj.get_progress_bar() + \
                     "Status: %s" % obj.get_status()
            self.progress_signal.emit(status)
            time.sleep(0.2)
        if obj.isSuccessful():
            self.progress_signal.emit("downloaded file to '%s'\n" % obj.get_dest() +
                                       "download task took %ss\n" % obj.get_dl_time(human=True) +
                                       "File hashes:\n" +
                                       " * MD5: %s\n" % obj.get_data_hash('md5') +
                                       " * SHA1: %s\n" % obj.get_data_hash('sha1') +
                                       " * SHA256: %s" % obj.get_data_hash('sha256')
                                       )
        else:
            self.progress_signal.emit("There were some errors:\n" +
                                       "\n".join([str(e) for e in obj.get_errors()]))

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startDownload)
        #self.progressBar = self.ui.progressBar

    def startDownload(self):
        url = self.ui.lineEdit.text()
        self.download_thread = DownloadThread(url)
        self.download_thread.progress_signal.connect(self.updateProgress)
        self.download_thread.start()

    def updateProgress(self, text):
        self.ui.textBrowser.setText(text)
        #self.progressBar.setValue(self.download_thread.obj.get_progress() * 100)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
