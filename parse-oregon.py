#!/usr/bin/env python

import pprint

prog_listing = {}
gone_to = {}

for i in open("oregon.bas", "r"):
    raw_string = i.rstrip("\r\n")
    split_string = raw_string.split(" ")
    line_num = split_string[0]
    prog_listing[line_num] = split_string[1:]

print(prog_listing)

for i in prog_listing.keys():
    if "GOTO" in prog_listing[i]:
        print(" ".join(prog_listing[i]))
        my_index = prog_listing[i].index("GOTO")
        my_dest = prog_listing[i][my_index + 1].split(",")
        for j in my_dest:
            if j in gone_to:
                gone_to[j].append(i)
            else:
                gone_to[j] = [i]
        print(my_index, my_dest)

pprint.pprint(gone_to)
