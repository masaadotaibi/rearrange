#!/usr/bin/env python3

import unittest
from rearrange import rearrange_name


class TestRearrange(unittest.TestCase):

    def test_basic(self):
        # arrange
        testcase = "Lovelace, Ada"

        # assign
        expected = "Ada Lovelace"

        # assert
        self.assertEqual(rearrange_name(testcase), expected)


    def test_empty(self):
        # arrange
        testcase = ""

        # assign
        expected = ""

        # assert
        self.assertEqual(rearrange_name(testcase), expected)

    def test_double_name(self):
        # arrange
        testcase = "Hopper, Grace M."

        # assign
        expected = "Grace M. Hopper"

        # assert
        self.assertEqual(rearrange_name(testcase), expected)


    def test_one_name(self):
        # arrange
        testcase = "Voltaire"

        # assign
        expected = "Voltaire"

        # assert
        self.assertEqual(rearrange_name(testcase), expected)


unittest.main()