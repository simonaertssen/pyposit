# -*- coding: utf-8 -*-
from src.posit import Posit

N = 1_000_00


def test_float_speed():
    for _ in range(N):
        0.1234567890 + 0.5678901234
        0.2345678901 + 0.6789012345
        0.3456789012 + 0.7890123456
        0.4567890123 + 0.8901234567
        0.5678901234 + 0.9012345678

        0.6789012345 + 0.0123456789
        0.7890123456 + 0.1234567890
        0.8901234567 + 0.2345678901
        0.9012345678 + 0.3456789012
        0.0123456789 + 0.4567890123


def test_posit_speed():
    for _ in range(N):
        Posit(0.1234567890) + Posit(0.5678901234)
        Posit(0.2345678901) + Posit(0.6789012345)
        Posit(0.3456789012) + Posit(0.7890123456)
        Posit(0.4567890123) + Posit(0.8901234567)
        Posit(0.5678901234) + Posit(0.9012345678)

        Posit(0.6789012345) + Posit(0.0123456789)
        Posit(0.7890123456) + Posit(0.1234567890)
        Posit(0.8901234567) + Posit(0.2345678901)
        Posit(0.9012345678) + Posit(0.3456789012)
        Posit(0.0123456789) + Posit(0.4567890123)

# if __name__ == "__main__":
#     start = time()
#     test_float_speed()
#     float_time = time() - start
#     print(f"Float addition takes {float_time:.2f}s for {10*N} repetitions")

#     start = time()
#     test_posit_speed()
#     posit_time = time() - start
#     print(f"Posit addition takes {posit_time:.2f}s for {10*N} repetitions, {posit_time/float_time:.2f} times slower")


if __name__ == "__main__":
    test = 0.2345
    print(test.__sizeof__())
    print(dir(test))
