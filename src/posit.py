from math import log2, ceil
from sys import getsizeof


class Posit(object):
    """Represents a posit number, a drop-in replacement for float."""

    def __init__(self, bits: str = '0', nbits: int = 16, es: int = 1) -> None:
        """Initialise the number and cast to desired format."""
        # Verify and add remaining leading 0s
        print(len(bits), nbits)
        assert(len(bits) <= nbits)
        bits = '0'*(nbits - len(bits)) + bits
        assert(len(bits) == nbits)

        self.nbits: int = nbits
        self.es: int = es
        self.useed: int = 2**(2**self.es)

        # Calculate indices of different parts
        regimelen: int = int(bits[1::], 2).bit_length()
        for i in (0, 1, 1 + regimelen, 1 + regimelen + es)
        self.bits: tuple[int] =

        self.sign: int = int(bits[0], 2)
        self.regime: int = int(bits[1:regimelen], 2)

        self.exponent: int = int(bits[regimelen:regimelen+es], 2)
        self.fraction: int = int(bits[regimelen+es::], 2)

        self.num_regime_bits: int = len(self.regime)
        self.num_exponent_bits: int = len(self.exponent)
        self.num_fraction_bits: int = len(self.fraction)

        self.k: int = self._run_length_encoding(self.regime)

    def _run_length_encoding(self, regime: int) -> int:
        """Turn the regime into a run-length encoded number k."""
        # First find leading 1s and 0s: https://skalkoto.blogspot.com/2008/01/bit-operations-find-first-zero-bit.html
        first_one: int = regime.bit_length()
        popcount: int = bin(regime).count("1")
        k = first_one - self.num_regime_bits
        if popcount > 1:
            k += popcount - 1
        return k

    def __repr__(self) -> str:
        return f"posit({self.to_float()})"

    def to_float(self) -> float:
        s: int = (-1)**(self.sign)
        r: int = self.useed**(self.k)
        e: int = self.base**(self.exponent)

        denum: int = 2**(ceil(log2(self.fraction + 1)))
        f: float = self.fraction / denum
        print(s, e, r, f)
        return s * r * e * (1 + f)

    def __add__(self, other: 'Posit') -> 'Posit':
        pass


if __name__ == "__main__":
    p1 = Posit(bits='0000110111011101', es=3)
    print(p1)

    # p2 = Posit()
    # print(p2)

    # p3 = p1 + p2
    # print(p3)

    number = 3
    print(number.bit_length())
