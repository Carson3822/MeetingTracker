import unittest
import attendance


class TestAttendance(unittest.TestCase):
    def test_sign_in_main_device1(self):
        test_param = "E01"
        result = attendance.sign_in_main_device(test_param)
        self.assertEqual(result, True)

    def test_sign_in_main_device2(self):
        test_param = "E01"
        result = attendance.sign_in_main_device(test_param)
        self.assertEqual(result, True)

    def test_auto_sign_out(self):
        pass