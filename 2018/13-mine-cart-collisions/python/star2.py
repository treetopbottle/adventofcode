#!/usr/bin/env python3


CARTS = ['<', '^', '>', 'v']


turns = {
    ('>', '\\'): 'v',
    ('>', '/'):  '^',
    ('<', '\\'): '^',
    ('<', '/'):  'v',
    ('^', '\\'): '<',
    ('^', '/'):  '>',
    ('v', '\\'): '>',
    ('v', '/'):  '<',
}


#with open('example2') as f:
with open('input') as f:
    track = [list(l[:-1]) for l in f.readlines()]

cart_nr = 0
cart_numbers = {}
cart_state = {}
empty_track = []
for j,row in enumerate(track):
    empty_row = ''
    for i,c in enumerate(row):
        if c in CARTS:
            cart_numbers[(i, j)] = cart_nr
            cart_state[cart_nr] = 0
            cart_nr += 1
        if c == '>' or c == '<':
            empty_row += '-'
        elif c == '^' or c == 'v':
            empty_row += '|'
        else:
            empty_row += c
    empty_track.append(empty_row)

collision = False
track = track
nr_carts = cart_nr-1
while nr_carts > 1:
    nr_carts = 0
    moved_carts = []
    for j,row in enumerate(track):
        for i,c in enumerate(row):
            if c not in CARTS:
                continue
            if (i,j) in moved_carts:
                continue

            # Determine direction
            if c == '>':
                new_i, new_j = (i+1, j)
            elif c == '<':
                new_i, new_j = (i-1, j)
            elif c == '^':
                new_i, new_j = (i, j-1)
            elif c == 'v':
                new_i, new_j = (i, j+1)

            new_c = c
            on_new_pos = track[new_j][new_i]
            if on_new_pos in CARTS:
                # remove both carts:
                collision = True
                new_c = empty_track[new_j][new_i]
                nr_carts -= 1
            elif on_new_pos in ['/', '\\']:
                new_c = turns[(c, on_new_pos)]
            elif on_new_pos in ['+']:
                state = cart_state[cart_numbers[(i, j)]]
                cart_index = CARTS.index(c)
                change = state - 1
                new_index = (cart_index + change) % len(CARTS)
                new_c = CARTS[new_index]
                cart_state[cart_numbers[(i, j)]] = (state + 1) % 3

            # Update track
            track[new_j][new_i] = new_c
            track[j][i] = empty_track[j][i]
            moved_carts.append((new_i, new_j))

            # Update cart locations
            cart_nr = cart_numbers.pop((i, j))
            cart_numbers[new_i, new_j] = cart_nr

            if new_c in CARTS:
                nr_carts += 1


for j,row in enumerate(track):
    for i,c in enumerate(row):
        if c in CARTS:
            print('{},{}'.format(i, j))

