import random


UP = "^"
DOWN = "v"
LEFT = "<"
RIGHT = ">"
ALL_DIRECTIONS = (UP, DOWN, LEFT, RIGHT)



print('x'*82)
for j in range(25):
    print('x%sx' % ''.join(random.choices(ALL_DIRECTIONS, k=80)))
print('x'*82)
