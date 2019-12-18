import sys
import os
import subprocess
from PyQt5.QtCore import *
from pytube import YouTube
from YouTubedwld import *


class YtDownloadThread(QThread):

    def __init__(self, parent=None):
        super(YtDownloadThread, self).__init__()
        self.yt_url = ""
        self.yt_savepath = ""
        self.yt_quality = ""

    def run(self):
        self.downloadyt(self.yt_url, self.yt_savepath, self.yt_quality)

        return True

    def downloadyt(self, url, savepath, quality):
        yt = YouTube(url)

        self.yt_url = url
        self.yt_savepath = savepath
        self.yt_quality = quality

        # 영상이 해당 화질을 갖고 있지 않을 시, 한 단계 아래 화질로 다운로드
        try:
            if(quality == 0):
                stream = yt.streams.get_by_itag("248")
                stream.download(savepath)
        except:
            stream = yt.streams.get_by_itag("247")
            stream.download(savepath)

        try:
            if(quality == 1):
                stream = yt.streams.get_by_itag("247")
                stream.download(savepath)
        except:
            stream = yt.streams.get_by_itag("135")
            stream.download(savepath)

        try:
            if(quality == 2):
                stream = yt.streams.get_by_itag("135")
                stream.download(savepath)
        except:
            stream = yt.streams.get_by_itag("18")
            stream.downlad(savepath)

        try:
            if(quality == 3):
                stream = yt.streams.get_by_itag("18")
                stream.download(savepath)
        except:
            stream = yt.stream.get_by_itag("133")
            stream.download(savepath)

        if(quality == 4):
            stream = yt.streams.get_by_itag("18")
            stream.download(savepath)
            self.default_filename = stream.default_filename
            subprocess.call(["ffmpeg", "-i",
                             os.path.join(savepath, self.default_filename),
                             os.path.join(savepath, "audio.mp3")
                             ])