#!/usr/bin/python3
"""this is a unit test for 6-max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """this is a unit test for max_integer([..])"""


    def test_no_arg(self):
        """this is another unit test for max_integer([..])"""
        self.assertEqual(max_integer(), None)

    def test_one(self):
        """this is another unit test for max_integer([..])"""
        self.assertEqual(max_integer([98]), 98)

    def test_begin_max(self):
        """this is another unit test for max_integer([..])"""
        self.assertEqual(max_integer([6, 5, 4, 3, 2, 1]), 6)

    def end_max(self):
        """this is another unit test for max_integer([..])"""
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_when_same(self):
        """this is another unit test for max_integer([..])"""
        self.assertEqual(max_integer([1, 1, 1, 1]), 1)

    def test_when_empty(self):
        """this is another unit test for max_integer([..])"""
        self.assertEqual(max_integer([]), None)

    def test_oneitem(self):
        """this is another unit test for max_integer([..])"""
        self.assertEqual(max_integer([42]), 42)

    def test_pos_neg(self):
        """this is another unit test for max_integer([..])"""
        self.assertEqual(max_integer([-1, 2, 6, -6]), 6)

    def test_floats(self):
        """this is another unit test for max_integer([..])"""
        self.assertEqual(max_integer([1.0, 10, .10, 10.1]), 10.1)

    def test_numstr(self):
        """this is another unit test for max_integer([..])"""
        self.assertEqual(max_integer("123456789"), "9")

    def strings_list(self):
        """this is another unit test for max_integer([..])"""
        self.assertEqual(max_integer(["aye", "bye", "cry", "die"]), ["die"])

    def empty_string(self):
        """this is another unit test for max_integer([..])"""
        self.assertEqual(max_integer(""), None)

    def infinity_test(self):
        """this is another unit test for max_integer([..])"""
        self.assertEqual(max_integer([42, float('inf'), float('-inf')]),
                         float('inf'))

    def type_mixed_pickles(self):
        """this is another unit test for max_integer([..])"""
        self.assertEqual(max_integer(["baby", "got", 500, "back"]), 500)

    def nan_test(self):
        """this is another unit test for max_integer([..])"""
        self.assertEqual(max_integer([float('nan'), 98, 99, 100]), 100 )

    def just_a_num(self):
        """this is another unit test for max_integer([..])"""
        with self.assertRaises(TypeError):
            max_integer(42)

    def just_a_float(self):
        """this is another unit test for max_integer([..])"""
        with selfassertRaises(TypeError):
            max_integer(4.2)

    def send_a_dict(self):
        """this is another unit test for max_integer([..])"""
        with selfassertRaises(TypeError):
            max_integer([{4: 2, 4: 2}, {"four": "two"}])



if __name__ == '__main__':
    unittest.main()
