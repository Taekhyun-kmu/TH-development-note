import unittest


from BackEnd import YtDownloadThread

class TestDownload(unittest.TestCase):
    def setUp(self):
        self.d = YtDownloadThread()

    def tearDown(self):
        pass

    def testDownloadyt(self):
        # 영상을 1080p로 바탕화면에 저장
        test1 = self.d.downloadyt("https://www.youtube.com/watch?v=yqtCGojXEpM", "C:/Users/SAMSUNG/Desktop", 0)
        self.assertEqual(self.d.yt_url, "https://www.youtube.com/watch?v=yqtCGojXEpM")
        self.assertEqual(self.d.yt_url, "")
        self.assertEqual(self.d.yt_savepath, "C:/Users/SAMSUNG/Desktop")
        self.assertEqual(self.d.yt_savepath, "")
        self.assertEqual(self.d.yt_quality, 3)
        self.assertEqual(self.d.yt_quality, 2)

        # 영상을 720p로 downloadtest라는 폴더에 저장
        test2 = self.d.downloadyt("https://www.youtube.com/watch?v=yqtCGojXEpM", "C:/Users/SAMSUNG/Desktop/downloadtest", 1)

        # 영상을 480p로 바탕화면에 저장
        test3 = self.d.downloadyt("https://www.youtube.com/watch?v=eP4ga_fNm-E", "C:/Users/SAMSUNG/Desktop", 2)

        # 영상을 360p로 바탕화면에 저장
        test4 = self.d.downloadyt("https://www.youtube.com/watch?v=yqtCGojXEpM", "C:/Users/SAMSUNG/Desktop", 3)

        # 영상을 다운로드 받고, MP3확장자로 변환하여 음원 추출
        test5 = self.d.downloadyt("https://www.youtube.com/watch?v=hROi9pWkZfE", "C:/Users/SAMSUNG/Desktop", 4)

        # 영상이 720p까지만 지원하는데 1080p로 다운받고자 하는 경우
        test6 = self.d.downloadyt("https://www.youtube.com/watch?v=hROi9pWkZfE", "C:/Users/SAMSUNG/Desktop", 0)

        # 영상이 480p까지만 지원하는데 720p로 다운받고자 하는 경우
        test7 = self.d.downloadyt("https://www.youtube.com/watch?v=x22TJMv2RYo", "C:/Users/SAMSUNG/Desktop", 1)

        # 영상이 240p 까지만 지원하는데 360p로 다운받고자 하는 경우
        test8 = self.d.downloadyt("https://www.youtube.com/watch?v=jNQXAC9IVRw", "C:/Users/SAMSUNG/Desktop", 3)


if __name__ == '__main__':
    unittest.main()