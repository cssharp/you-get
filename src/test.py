#!/usr/bin/env python

import unittest

from you_get.extractors import (
    qq,
)


class YouGetTests(unittest.TestCase):
    def test_qq(self):
        qq.download('https://v.qq.com/x/page/p00298x0nm0.html', info_only=True)#no
        qq.download('https://v.qq.com/x/page/x0822duagxm.html', info_only=True)#ok



if __name__ == '__main__':
    unittest.main()
