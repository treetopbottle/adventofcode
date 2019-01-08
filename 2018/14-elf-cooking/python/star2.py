#!/usr/bin/env python3

with open('input') as f:
    pattern = f.read().strip()

recipe_board = '37'
elf1 = 0
elf2 = 1

# Two recipes can be added in one turn, so check an extra character for
# pattern: -len(pattern)-1
while not pattern in recipe_board[-len(pattern)-1:]:
    new_score = int(recipe_board[elf1]) + int(recipe_board[elf2])
    recipe_board += str(new_score)
    elf1 = (elf1 + 1 + int(recipe_board[elf1])) % len(recipe_board)
    elf2 = (elf2 + 1 + int(recipe_board[elf2])) % len(recipe_board)
    assert elf1 != elf2

nr_recipes = len(recipe_board) - len(pattern)
if not recipe_board.endswith(pattern):
    nr_recipes -= 1
print(nr_recipes)
