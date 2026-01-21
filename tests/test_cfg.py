import unittest
from mypkg.cfg import Config

class TestCfg(unittest.TestCase):

    def test_basix(self):
        my_cfg = Config()
        my_cfg.inject({'bar': 'foo', 'id': 666})

        self.assertEqual('foo', my_cfg._cfg['bar'])
        self.assertEqual(666, my_cfg._cfg['id'])

if __name__ == '__main__':
    unittest.main()