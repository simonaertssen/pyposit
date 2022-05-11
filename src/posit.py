# -*- coding: utf-8 -*-
from math import log2, ceil

from src.errors import NotSupportedError, BitSizeError


class Posit(object):
    """Represents a posit number, a drop-in replacement for float."""

    def __init__(self, bits: str, numbits: int = 16, es: int = 1) -> None:
        """Initialise the number and extract the different posit pieces."""
        # Verify input
        if not isinstance(bits, str):
            raise NotSupportedError(f"{type(bits)} is not supported.")

        if numbits not in (8, 16, 32, 64):
            raise BitSizeError()

        if bits.startswith("0b"):
            bits.removeprefix("0b")

        bitlen: int = len(bits)
        if bitlen > numbits:
            raise ValueError(f"{bits} contains {len(bits)} > {numbits}")

        # Fixed values
        self.bits: str = bits
        self.numbits: int = numbits
        self.es: int = es
        self.useed: int = 2**(2**self.es)

        # Preallocate for switching between states
        self.sign: int = 0
        self.regime: int = 0
        self.exponent: int = 0
        self.fraction: int = 0

        self.k: int = 0
        self.signlen: int = 1
        self.regimelen: int = 0
        self.fraclen: int = 0

        # Now register the correct values for sign, regime, exponent and fraction
        bits = '0' * (numbits - bitlen) + bits
        self.sign: int = int(bits[0], base=2)

        # Start of the regime is where bits differ
        firstbit: int = int(bits[1], base=2)

        self.regimelen = 1  # + 1 for sign offset
        try:  # whether any change occurs in the entire bitarray
            self.regimelen += bits[1:].index(str(1 - firstbit))
        except ValueError:
            self.regimelen = numbits - 1
        else:
            self.regimelen += 1  # + 1 including the index in the range
        assert 1 < self.regimelen < numbits

        self.regime = int(bits[1:self.regimelen], base=2)
        self.k = firstbit * (self.regimelen - 3) - (1 - firstbit) * (self.regimelen - 2)

        # Set in case of extremes: 0 or infinity
        if bits == '0' * numbits:
            self.sign = 0
            return
        elif bits == '1' + '0' * (numbits - 1):
            self.sign = 1
            return

        self.exponent = int(bits[self.regimelen:self.regimelen + es], base=2)
        self.fraction = int(bits[self.regimelen + es:], base=2)
        self.fraclen = numbits - self.signlen - self.regimelen - es
        assert numbits == self.signlen + self.regimelen + self.es + self.fraclen

    def __repr__(self) -> str:
        return f"posit({self.to_float()})"

    def to_float(self) -> float:
        s: int = (-1)**(self.sign)
        r: int = self.useed**(self.k)
        e: int = 2**(self.exponent)

        denum: int = 2**(ceil(log2(self.fraction + 1)))
        f: float = self.fraction / denum
        return s * r * e * (1 + f)

    def __add__(self, other: 'Posit') -> 'Posit':
        pass


if __name__ == "__main__":
    p1 = Posit(bits='0000110111011101', es=3)
    print(p1)
    # p1 = Posit(bits='00001000', es=3)
    # print(p1)
