"""
Program: test_basic_list.py
Author:  Spencer Cress
Date: 06/20/2020

Tests for basic list functions
"""
import unittest
# import unittest.mock as mock
from Module7.fun_with_collections import basic_list as topic1
from unittest.mock import patch


class TestList(unittest.TestCase):
    """Tests make list function to make sure it returns a numeric list"""
    @patch('basic_list.get_input', return_value='5')
    def test_make_list(self, input):
        self.assertEqual(topic1.make_list(), [5, 5, 5])


if __name__ == '__main__':
    unittest.main()
