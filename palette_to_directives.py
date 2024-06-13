#!/usr/bin/env python3

# Convert a palette from colorzilla.com to 68k assembly directives
# Copyright (C) 2024 Francesco Palazzo

import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python palette_to_directives.py <palette_file>")
        sys.exit(1)

    with open(sys.argv[1], "r") as f:
        lines = f.readlines()

    with open("directives.txt", "w") as f:
        f.write(" " * 8 + "org $040000\n")
        row = []
        for line in lines:
            line = line.strip()
            if not line:
                continue
            rgb = line.split()[:3]
            row.extend(rgb)
            if len(row) == 3*8:
                f.write(" " * 8 + "dc.b " + ",".join(row) + "\n")
                row = []

if __name__ == "__main__":
    main()
