import unittest

import day1


class MyTestCase(unittest.TestCase):
    # Part 1
    def test_case_1(self):
        self.assertEqual(day1.captcha("1122", False), 3)

    def test_case_2(self):
        self.assertEqual(day1.captcha("11", False), 2)

    def test_case_3(self):
        self.assertEqual(day1.captcha("1234", False), 0)

    def test_case_4(self):
        self.assertEqual(day1.captcha("91212129", False), 9)

    # Part 2
    def test_case_5(self):
        self.assertEqual(day1.captcha("1212", True), 6)

    def test_case_6(self):
        self.assertEqual(day1.captcha("123123", True), 12)

if __name__ == '__main__':
    unittest.main()
