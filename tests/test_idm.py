import unittest
from mypkg.idm import User



class TestIdm(unittest.TestCase):

    def test_basix(self):

        id=42
        user='svenschrodt'
        passw='oez t8vbztp9w8'

        sven = User(id=id, user=user, passw=passw, groups=[])

        self.assertEqual(sven.id, id)
        self.assertEqual(sven.user, user)
        self.assertEqual(sven.passw, passw)


if __name__ == '__main__':
    unittest.main()