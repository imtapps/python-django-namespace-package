import unittest

from sample.main import one

class SampleOneTest(unittest.TestCase):

    def test_one(self):
        self.assertEqual(one.ONE, 1)