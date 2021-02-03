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

print('success')

'''
# 1.16.5
# {
#   "Name": "minecraft:white_carpet"
# }
#
# 1.12.2
# {
#   "Properties": {
#     "color": "white"
#   },
#   "Name": "minecraft:carpet"
# }

def make_carpet(color):
    return nbtlib.Compound({
        'Name': nbtlib.String('minecraft:carpet'),
        'Properties': nbtlib.Compound({
            'color': nbtlib.String(color)
        })
    })

# 1.16.5
# {
#   'Name': 'minecraft:white_terracotta'
# }
#
# 1.12.2
# {
#   'Properties': {
#     'color': 'white'
#   },
#   'Name': 'minecraft:stained_hardened_clay'
# }

def make_terracotta(color):
    return nbtlib.Compound({
        'Name': nbtlib.String('minecraft:hardened_clay'),
        'Properties': nbtlib.Compound({
            'color': nbtlib.String(color)
        })
    })

trans = {
    # Carpet
    'minecraft:white_carpet': make_carpet('white'),
    'minecraft:orange_carpet': make_carpet('orange'),
    'minecraft:magenta_carpet': make_carpet('magenta'),
    'minecraft:light_blue_carpet': make_carpet('light_blue'),
    'minecraft:yellow_carpet': make_carpet('yellow'),
    'minecraft:lime_carpet': make_carpet('lime'),
    'minecraft:pink_carpet': make_carpet('pink'),
    'minecraft:gray_carpet': make_carpet('gray'),
    'minecraft:light_gray_carpet': make_carpet('light_gray'),
    'minecraft:cyan_carpet': make_carpet('cyan'),
    'minecraft:purple_carpet': make_carpet('purple'),
    'minecraft:blue_carpet': make_carpet('blue'),
    'minecraft:brown_carpet': make_carpet('brown'),
    'minecraft:green_carpet': make_carpet('green'),
    'minecraft:red_carpet': make_carpet('red'),
    'minecraft:black_carpet': make_carpet('black'),
    # Terracotta
    'minecraft:white_terracotta': make_terracotta('white'),
    'minecraft:orange_terracotta': make_terracotta('orange'),
    'minecraft:magenta_terracotta': make_terracotta('magenta'),
    'minecraft:light_blue_terracotta': make_terracotta('light_blue'),
    'minecraft:yellow_terracotta': make_terracotta('yellow'),
    'minecraft:lime_terracotta': make_terracotta('lime'),
    'minecraft:pink_terracotta': make_terracotta('pink'),
    'minecraft:gray_terracotta': make_terracotta('gray'),
    'minecraft:light_gray_terracotta': make_terracotta('light_gray'),
    'minecraft:cyan_terracotta': make_terracotta('cyan'),
    'minecraft:purple_terracotta': make_terracotta('purple'),
    'minecraft:blue_terracotta': make_terracotta('blue'),
    'minecraft:brown_terracotta': make_terracotta('brown'),
    'minecraft:green_terracotta': make_terracotta('green'),
    'minecraft:red_terracotta': make_terracotta('red'),
    'minecraft:black_terracotta': make_terracotta('black')
}

with nbtlib.load(sys.argv[1]) as f:
    palette = f.root['palette']
    for i in range(len(palette)):
        if str(palette[i]['Name']) in trans.keys():
            palette[i] = trans[str(palette[i]['Name'])]
'''
