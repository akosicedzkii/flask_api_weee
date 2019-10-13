import unittest
import sys
sys.path.append('../')
import send_email


class TestRun(unittest.TestCase):

    def test_send_email(self):
        result = send_email.send_message("test","test","cedzkii81@gmail.com")
        self.assertEqual(None,result)

if __name__ == '_main_':
    unittest.main()
