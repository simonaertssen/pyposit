# -*- coding: utf-8 -*-
from time import time
from math import floor, log10

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


if __name__ == "__main__":
    start = time()
    test_float_speed()
    float_time = time() - start

    conversion = {0: "", 1: "kilo", 2: "mega", 3: "giga", 4: "tera"}
    flops = (10.0 * N) / float_time
    base = floor(log10(flops) / 3.0)

    print(f"Float addition: {(10 * N / float_time) * 10**(-base * 3.0):.0f} {conversion[base]}FLOPS")
