#!/usr/bin/env python3

import math

# Generates a table of 256 sin values in hex format for M68K
# Copyright (C) 2024 Francesco Palazzo

def hex_sin(x_norm):
    return int(128*math.sin(x_norm*math.pi/256))

def main():
    with open('sin_table.txt', 'w') as f:
        row = []
        for i in range(0, 256):
            if i & 0x80:
                i = i - 256
            sin_value = hex_sin(i)
            row.append(sin_value)
            if i % 16 == 15:
                f.write(f'        dc.b {",".join([str(x) for x in row])}\n')
                row = []

if __name__ == '__main__':
    main()
