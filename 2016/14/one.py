#!/usr/bin/env python3

import fileinput
import hashlib
import sys

salt = fileinput.input()[0].strip()
index = 0


def find_triplet(string):
    for i in range(1,len(md5_hash)-1):
        if md5_hash[i-1] == md5_hash[i] and md5_hash[i] == md5_hash[i+1]:
            return md5_hash[i]
    return False

def find_quintuples(string):
    founds = []
    for i in range(2,len(md5_hash)-2):
        if md5_hash[i-2] == md5_hash[i-1] \
            and md5_hash[i-1] == md5_hash[i] \
            and md5_hash[i] == md5_hash[i+1] \
            and md5_hash[i+1] == md5_hash[i+2]:
            founds.append(md5_hash[i])
    return founds


triplets = {}
quintuplets = {}

for index in range(2**16):
    si = (salt + str(index)).encode('utf-8')
    md5_hash = hashlib.md5(si).hexdigest()
    char3 = find_triplet(md5_hash)
    if char3:
        #print('3', index, char3, si, md5_hash)
        triplets[index] = char3

    char5s = find_quintuples(md5_hash)
    for char5 in char5s:
        #print('5', index, char5, si, md5_hash)
        try:
            quintuplets[char5].append(index)
        except KeyError:
            quintuplets[char5] = [index]


keys = 0
for index in sorted(triplets.keys()):
    char = triplets[index]
    try:
        qs = quintuplets[char]
        for q in qs:
            if index < q and q < index+1000:
                keys += 1
                print(index, char, q)
                break
    except KeyError:
        pass
    if keys == 64:
        print(index)
        break

fileinput.close()

