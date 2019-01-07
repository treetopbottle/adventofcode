#!/usr/bin/env python3


PADDING = '..'
NR_GENERATIONS = 20


def next_gen(pots, rewrite_rules):
    new_pots = PADDING
    for i in range(len(PADDING), len(pots)-len(PADDING)):
        area = pots[i-2:i+3]
        new_pots += rewrite_rules[area]
    return new_pots + PADDING


rewrite_rules = {}
with open('input') as f:
    lines = f.readlines()
    initial_state = lines[0][15:].strip()
    for line in lines[2:]:
        rewrite_rules[line[:5]] = line[9]

# Add padding to the pots string to allow growth. For example, this rule would
# grow a plant two pots further left:
#   ....# => #
pots = PADDING + \
    PADDING*NR_GENERATIONS + \
    initial_state + \
    PADDING*NR_GENERATIONS + \
    PADDING
# Determine pot numbers for scoring
first_pot_nr = -1*(NR_GENERATIONS+1)*len(PADDING)
last_pot_nr = first_pot_nr + len(pots)

for _ in range(NR_GENERATIONS):
    pots = next_gen(pots, rewrite_rules)

total_sum = 0
for i, pot_nr in enumerate(range(first_pot_nr, last_pot_nr)):
    if pots[i] == '#':
        total_sum += pot_nr

print(total_sum)
