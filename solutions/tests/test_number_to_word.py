#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for conversion from number to word.

This module contains unittest test and edge cases for the number_to_word

Created on 03 01 2025
@author: Terry Aziaba
"""

import unittest

from ..number_to_word import number_to_word


class TestNumberToWord(unittest.TestCase):
    """Unit tests for the number_to_word function."""

    def test_valid_single_digits(self):
        """Test valid single-digit inputs."""
        self.assertEqual(number_to_word(0), "zero")
        self.assertEqual(number_to_word(1), "one")
        self.assertEqual(number_to_word(2), "two")
        self.assertEqual(number_to_word(3), "three")
        self.assertEqual(number_to_word(4), "four")
        self.assertEqual(number_to_word(5), "five")
        self.assertEqual(number_to_word(6), "six")
        self.assertEqual(number_to_word(7), "seven")
        self.assertEqual(number_to_word(8), "eight")
        self.assertEqual(number_to_word(9), "nine")

    def test_invalid_numbers(self):
        """Test invalid numbers that are not single digits."""
        with self.assertRaises(ValueError):
            number_to_word(10)  # Two-digit number
        with self.assertRaises(ValueError):
            number_to_word(-1)  # Negative number
        with self.assertRaises(ValueError):
            number_to_word(100)  # Larger number

    def test_non_integer_inputs(self):
        """Test inputs that are not integers."""
        with self.assertRaises(ValueError):
            number_to_word(3.5)  # Float input
        with self.assertRaises(ValueError):
            number_to_word("three")  # String input
        with self.assertRaises(ValueError):
            number_to_word(None)  # NoneType input

    def test_edge_cases(self):
        """Test edge cases like boundary values."""
        self.assertEqual(number_to_word(0), "zero")  # Lower boundary
        self.assertEqual(number_to_word(9), "nine")  # Upper boundary
