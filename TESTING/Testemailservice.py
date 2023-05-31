import unittest
import emailservice

class TestEmailService(unittest.TestCase):
    def test_email1(self):
        test_param = 0
        result = emailservice.create_MIME_msg(test_param)
