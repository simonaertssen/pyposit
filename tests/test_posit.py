# -*- coding: utf-8 -*-
import unittest
from src.posit import Posit


class PositTester(unittest.TestCase):

    def setUp(self) -> None:
        self.p: Posit = Posit(bits='00000000', numbits=8)

    def test_initialization(self) -> None:
        """Test whether the posit was initialised well."""
        self.p.__init__(bits='00000000', numbits=8)
        self.assertEqual(self.p.sign, 0)
        self.assertEqual(self.p.regime, 0)
        self.assertEqual(self.p.exponent, 0)
        self.assertEqual(self.p.fraction, 0)

        self.p.__init__(bits='10000000', numbits=8)
        self.assertEqual(self.p.sign, 1)
        self.assertEqual(self.p.regime, 0)
        self.assertEqual(self.p.exponent, 0)
        self.assertEqual(self.p.fraction, 0)

        self.p.__init__('0000110111011101', numbits=16, es=3)
        self.assertEqual(self.p.sign, int('0', base=2))
        self.assertEqual(self.p.regime, int('0001', base=2))
        self.assertEqual(self.p.exponent, int('101', base=2))
        self.assertEqual(self.p.fraction, int('11011101', base=2))

    def test_run_length_encoding(self) -> None:
        """Test the correctness of the ruin length encoding of k."""
        regimes: list[int] = ['0001', '0010', '0100', '1000', '1100', '1110']
        expected_k: list[int] = [-3, -2, -1, 0, 1, 2]

        for regime, k in zip(regimes, expected_k):
            self.p.__init__(bits='0' + regime + '101', numbits=8, es=1)
            self.assertEqual(self.p.k, k)

    def test_float_representation(self) -> None:
        """Test the representation of a posit as a float."""
        self.p.__init__('0000110111011101', numbits=16, es=3)
        self.assertEqual(self.p.to_float(), 477 / 134217728.0)

    def test_addition(self) -> None:
        """Test whether the posit addition is correct."""


if __name__ == "__main__":
    unittest.main()
