import unittest

class TestFoo(unittest.TestCase):

    def test_basix(self):
        self.assertEqual(23, 11+12)

if __name__ == '__main__':
    unittest.main()