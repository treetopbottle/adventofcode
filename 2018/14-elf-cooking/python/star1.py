#!/usr/bin/env python3

SCORE_LEN = 10

with open('input') as f:
    nr_recipes = int(f.read().strip())

recipe_board = '37'
elf1 = 0
elf2 = 1

while len(recipe_board) < nr_recipes + SCORE_LEN:
    new_score = int(recipe_board[elf1]) + int(recipe_board[elf2])
    recipe_board += str(new_score)
    elf1 = (elf1 + 1 + int(recipe_board[elf1])) % len(recipe_board)
    elf2 = (elf2 + 1 + int(recipe_board[elf2])) % len(recipe_board)
    assert elf1 != elf2

print(recipe_board[nr_recipes:nr_recipes+SCORE_LEN])
