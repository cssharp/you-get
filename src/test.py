#!/usr/bin/env python

import unittest

from you_get.extractors import (
    qq,
)


class YouGetTests(unittest.TestCase):
    def test_qq(self):
        qq.download('https://v.qq.com/x/page/o0814y56zz5.html', info_only=True)
        #qq.download('https://v.qq.com/x/cover/2j5kilwvtepehti/u00298ogwed.html', info_only=True)

    

if __name__ == '__main__':
    unittest.main()
