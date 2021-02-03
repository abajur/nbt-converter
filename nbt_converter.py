#!/usr/bin/env python3

# Tool for converting Minecraft 1.16.5 Named Binary Tag (NBT) files to
# Minecraft 1.12.2 NBT files.

import nbtlib
import sys

if len(sys.argv) != 2:
    print(f'usage: {sys.argv[0]} <file>')
    sys.exit(1)

palette_1_12_2 = []
with open('palette-1.12.2.txt') as f:
    for line in f.readlines():
        line = line.strip()
        if len(line) == 0 or line[0] == '#':
            continue
        palette_1_12_2.append(nbtlib.parse_nbt(line))

palette_1_16_5 = []
with open('palette-1.16.5.txt') as f:
    for line in f.readlines():
        line = line.strip()
        if len(line) == 0 or line[0] == '#':
            continue
        palette_1_16_5.append(nbtlib.parse_nbt(line))

assert len(palette_1_12_2) == len(palette_1_16_5)

with nbtlib.load(sys.argv[1]) as f:
    palette = f.root['palette']
    for i in range(len(palette)):
        if palette[i] in palette_1_16_5:
            palette[i] = palette_1_12_2[palette_1_16_5.index(palette[i])]
