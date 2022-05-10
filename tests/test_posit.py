# -*- coding: utf-8 -*-
import unittest
from posit import Posit


class PositTester(unittest.TestCase):

    def setUp(self) -> None:
        self.p: Posit = Posit()

    def test_initialization(self) -> None:
        """Test whether the posit was initialised well."""
        self.p.__init__(sign='0', regime='0', exponent='0', fraction='0')
        self.assertEqual(self.p.sign, 0)
        self.assertEqual(self.p.regime, 0)
        self.assertEqual(self.p.exponent, 0)
        self.assertEqual(self.p.fraction, 0)
        self.assertEqual(self.p.num_regime_bits, 1)
        self.assertEqual(self.p.num_exponent_bits, 1)
        self.assertEqual(self.p.num_fraction_bits, 1)

        self.p.__init__(sign='0', regime='0001', exponent='101', fraction='11011101')
        self.assertEqual(self.p.sign, 0)
        self.assertEqual(self.p.regime, 1)
        self.assertEqual(self.p.exponent, 5)
        self.assertEqual(self.p.fraction, 221)
        self.assertEqual(self.p.num_regime_bits, 4)
        self.assertEqual(self.p.num_exponent_bits, 3)
        self.assertEqual(self.p.num_fraction_bits, 8)

    def test_run_length_encoding(self) -> None:
        """Test the correctness of the ruin length encoding of k."""
        self.p.__init__(regime='1000')  # Initialise with a correct regime length

        regimes: list[int] = [0b0000, 0b0001, 0b0010, 0b0100, 0b1000, 0b1100, 0b1110, 0b1111]
        expected_k: list[int] = [-4, -3, -2, -1, 0, 1, 2, 3]

        for regime, k in zip(regimes, expected_k):
            # self.p._run_length_encoding(regime)
            self.assertEqual(self.p._run_length_encoding(regime), k)

    def test_addition(self) -> None:
        """Test whether the posit addition is correct."""


if __name__ == "__main__":
    unittest.main()
