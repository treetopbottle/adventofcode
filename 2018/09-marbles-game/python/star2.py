#!/usr/bin/env python3

from collections import defaultdict, deque

nr_players = 0
last_marble = 0

with open('input') as f:
    line = f.readlines()[0]
    words = line.split(' ')
    nr_players = int(words[0])
    last_marble = int(words[6])
last_marble *= 100

player_scores = defaultdict(int)

circle = deque([0])
player = 0

for marble_nr in range(1, last_marble+1):
    if marble_nr % 23 == 0:
        player_scores[player] += marble_nr
        circle.rotate(7)
        player_scores[player] += circle.popleft()
    else:
        circle.rotate(-2)
        circle.appendleft(marble_nr)
    player = (player + 1) % nr_players

print(max(player_scores.values()))
