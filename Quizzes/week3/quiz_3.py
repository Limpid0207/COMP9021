# Written by *** for COMP9021

# Prompts the user for a positive integer.
# - When written in base 3, its consecutive digits read
#   from left to right represent the directions to take, with
#   * 0 meaning going South,
#   * 1 meaning South West,
#   * 2 meaning South East.
#
# Prints out:
# - the representation of the integer in base 3;
# - the corresponding sequence of directions to take, as arrows;
# - the sequence of arrows again, but nicely displayed.
#
# The leftmost arrow is printed out with no space to the left.
#
# The arrows are the Unicode characters of code point
# 0x21e9 and 0x2b02 and 0x2b03.

import sys

try:
    encoded_directions = int(input('Enter a positive integer: '))
    if encoded_directions < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

# INSERT YOUR CODE HERE
def into_arrow(n):
    if n == 0:
        return chr(0x21e9)
    elif n == 1:
        return chr(0x2b03)
    elif n == 2:
        return chr(0x2b02)

def decimal_into_ternary(decimal):
    base_3 = [decimal % 3]
    while decimal >= 3:
        decimal = decimal // 3
        base_3.append(decimal % 3)
    base_3.reverse()
    return base_3

def direction(dir):
    if int(dir) == 0:
        return 0
    elif int(dir) == 1:
        return -1
    elif int(dir) == 2:
        return 1

def max_nub_of_space(list):
    direction_list = [direction(i) for i in list]
    max_nub = min([sum(direction_list[:j]) for j in range(len(direction_list))])
    if max_nub >=0:
        return 0
    elif max_nub < 0:
        return -max_nub


ternary = decimal_into_ternary(int(encoded_directions))
print(f"In base 3, the input reads as: {''.join(str(t) for t in ternary)}")
print()
arrow = [into_arrow(n) for n in ternary]
print(f"So that's how you want to go: {''.join(str(a) for a in arrow)}")
print()
print("Let's go then!")
step = max_nub_of_space(ternary)
for t in ternary:
    print(step * ' ' + into_arrow(t))
    step += direction(int(t))

