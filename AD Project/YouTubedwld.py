import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, \
    QPushButton, QTextEdit, QLineEdit, QLabel, QFileDialog, QComboBox, QStatusBar

from BackEnd import *

class MyWindow(QWidget):

    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.initUI()
        self.setFixedSize(820, 400)
        self.ytdwnldthread = YtDownloadThread()
        self.show()

    def initUI(self):
        hbox1 = QHBoxLayout()
        YouTubeLink = QLabel("YouTube Link:", self)
        self.youtubelink = QLineEdit("", self)
        choosequality = QLabel("Quality:", self)
        self.choosequality = QComboBox()
        self.choosequality.addItems(["1080p", "720p", "480p", "360p", "Audio Only"])
        download_Button = QPushButton("다운받기")
        download_Button.clicked.connect(self.download_clicked)

        hbox1.addWidget(YouTubeLink)
        hbox1.addWidget(self.youtubelink)
        hbox1.addWidget(choosequality)
        hbox1.addWidget(self.choosequality)
        hbox1.addWidget(download_Button)

        hbox2 = QHBoxLayout()
        self.showprogress = QTextEdit()
        self.showprogress.setFixedSize(800, 270)
        self.showprogress.setReadOnly(True)
        self.showprogress.append("<span style='color:red'>*** How to Use ***</span>")
        self.showprogress.append("1. 유튜브 링크를 입력해주세요.")
        self.showprogress.append("2. 원하는 화질을 선택해주세요.")
        self.showprogress.append("3. 저장 경로를 설정해주세요.")
        self.showprogress.append("4. 다운받기 버튼을 누르면 다운로드가 시작됩니다.")

        hbox2.addWidget(self.showprogress)

        hbox3 = QHBoxLayout()
        self.find_Button = QPushButton("저장 경로")
        self.find_Button.clicked.connect(self.saveDirectory_clicked)
        self.textedit = QTextEdit()
        self.textedit.setFixedSize(680, 27)
        self.textedit.setReadOnly(True)
        hbox3.addWidget(self.textedit)
        hbox3.addWidget(self.find_Button)

        hbox4 = QHBoxLayout()
        self.statusbar = QStatusBar(self)
        hbox4.addWidget(self.statusbar)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox4)
        self.setLayout(vbox)
        self.setWindowTitle("YouTube Downloader")
        self.move(400, 200)
        self.show()


    def saveDirectory_clicked(self):
        self.savepath = QFileDialog.getExistingDirectory(self, "Select Directory")
        self.textedit.setText(self.savepath)


    def download_clicked(self):
        self.ytdwnldthread.yt_url = self.youtubelink.text()
        try:
            self.ytdwnldthread.yt_savepath = self.savepath
        except:
            self.ytdwnldthread.yt_savepath = os.path.expanduser("~\Desktop")
        self.ytdwnldthread.yt_quality = self.choosequality.currentIndex()
        self.statusbar.showMessage("다운로드를 시작합니다...")
        try:
            download = self.ytdwnldthread.run()
        except AttributeError:
            self.statusbar.showMessage("지원하지 않는 화질입니다. 더 낮은 화질을 선택해주세요!")
        except:
            self.statusbar.showMessage("유효한 링크가 아닙니다. 링크를 확인해주세요!")
        try:
            if download:
                self.statusbar.showMessage("다운로드 성공!")
        except:
            pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MyWindow()
    main.show()
    sys.exit(app.exec_())