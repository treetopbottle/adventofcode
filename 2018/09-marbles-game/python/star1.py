#!/usr/bin/env python3

from collections import defaultdict

nr_players = 0
last_marble = 0

with open('input') as f:
    line = f.readlines()[0]
    words = line.split(' ')
    nr_players = int(words[0])
    last_marble = int(words[6])

player_scores = defaultdict(int)

# Already do first three moves
assert nr_players > 2
assert last_marble > 2
circle = [0, 2, 1]
player = 3
index = 1

for marble_nr in range(player, last_marble+1):
    if marble_nr % 23 == 0:
        player_scores[player] += marble_nr
        index = (index - 7 + len(circle)) % len(circle)
        player_scores[player] += circle.pop(index)
    else:
        index = (index + 2) % len(circle)
        circle.insert(index, marble_nr)
    player = (player + 1) % nr_players

print(max(player_scores.values()))
