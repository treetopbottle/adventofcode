#!/usr/bin/env python3

import sys
import collections
import re

file_name = sys.argv[1]

with open(file_name) as f:
    passphrases = f.read()

    passphrases = re.split('\n', passphrases)
    valid = 0
    for passphrase in passphrases:
        if not passphrase:
            continue

        p = passphrase.split(' ')
        print(''.join(sorted(p[0])))
        p = [''.join(sorted(i)) for i in p]
        if len(p) == len(set(p)):
            valid += 1
            print(passphrase)
        else:
            pass

    print(valid)


