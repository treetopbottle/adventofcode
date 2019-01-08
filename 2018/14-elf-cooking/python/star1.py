#!/usr/bin/env python3

NR_RECIPES_FOR_SCORE = 10

with open('input') as f:
    nr_recipes_before_score = int(f.read().strip())

recipe_board = [3, 7]
elf1 = 0
elf2 = 1

desired_board_length = (nr_recipes_before_score + NR_RECIPES_FOR_SCORE)
while len(recipe_board) < desired_board_length:
    new_score = recipe_board[elf1] + recipe_board[elf2]
    new_recipes = [int(s) for s in list(str(new_score))]
    recipe_board.extend(new_recipes)
    elf1 = (elf1 + 1 + recipe_board[elf1]) % len(recipe_board)
    elf2 = (elf2 + 1 + recipe_board[elf2]) % len(recipe_board)
    assert elf1 != elf2

start = nr_recipes_before_score
end = nr_recipes_before_score+NR_RECIPES_FOR_SCORE
str_scores = [str(i) for i in recipe_board[start:end]]
print(''.join(str_scores))
