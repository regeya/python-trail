#!/usr/bin/env python

import pprint
import re

prog_listing = {}
gone_to = {}

for i in open("oregon.bas", "r"):
    raw_string = i.rstrip("\r\n")
    raw_string = re.sub(r", ", ",", raw_string)
    split_string = raw_string.split(" ")
    line_num = split_string[0]
    prog_listing[line_num] = split_string[1:]

for i in prog_listing.keys():
    if "GOTO" in prog_listing[i]:
        my_index = prog_listing[i].index("GOTO")
        my_dest = prog_listing[i][my_index + 1]
        pprint.pprint(my_dest)
        my_dest = re.sub(r"\s+", "", my_dest)
        my_dest = my_dest.split(",")
        pprint.pprint(my_dest)
        for j in my_dest:
            if j in gone_to:
                gone_to[j.strip()].append(i.strip())
            else:
                gone_to[j.strip()] = [i.strip()]

pprint.pprint(gone_to)
