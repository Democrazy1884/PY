import unittest
import cv2
import sys
from fight import startfind, gofind, boostfind, mainpagefind, mainpage_marchfind
from fight import endfind, fullfind, offlinefind, firstpagefind, marchfind


class Test(unittest.TestCase):

    def find(self, func1, func2, number):
        import os
        text = func1.__name__
        string = sys.path[0] + '\\test\\' + text + ('\\%d.jpg ' % number)
        # print(string)
        if os.path.exists(string):
            img = cv2.imread(string)
            x = func1(img)
            func2(x)

    def test_startfind(self):
        Test.find(self, startfind, self.assertTrue, 1)
        Test.find(self, startfind, self.assertTrue, 2)
        Test.find(self, startfind, self.assertFalse, 3)

    def test_gofind(self):
        Test.find(self, gofind, self.assertTrue, 1)
        Test.find(self, gofind, self.assertFalse, 2)

    def test_boostfind(self):
        Test.find(self, boostfind, self.assertTrue, 1)
        Test.find(self, boostfind, self.assertFalse, 2)

    def test_endfind(self):
        Test.find(self, endfind, self.assertTrue, 1)
        Test.find(self, endfind, self.assertFalse, 2)

    def test_fullfind(self):
        Test.find(self, fullfind, self.assertTrue, 1)
        Test.find(self, fullfind, self.assertFalse, 2)

    def test_offlinefind(self):
        Test.find(self, offlinefind, self.assertTrue, 1)
        Test.find(self, offlinefind, self.assertFalse, 2)

    def test_firstpagefind(self):
        Test.find(self, firstpagefind, self.assertTrue, 1)
        Test.find(self, firstpagefind, self.assertFalse, 2)

    def test_mainpagefind(self):
        Test.find(self, mainpagefind, self.assertTrue, 1)
        Test.find(self, mainpagefind, self.assertFalse, 2)

    def test_mainpage_marchfind(self):
        Test.find(self, mainpage_marchfind, self.assertTrue, 1)
        Test.find(self, mainpage_marchfind, self.assertFalse, 2)

    def test_marchfind(self):
        Test.find(self, marchfind, self.assertTrue, 1)
        Test.find(self, marchfind, self.assertFalse, 2)


if __name__ == "__main__":
    unittest.main()
