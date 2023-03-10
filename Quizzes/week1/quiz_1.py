# Written by *** and Eric Martin for COMP9021
#
# Generates a random list of integers between 1 and 9
# whose length is chosen by the user and displays the list.
# - If first and last number in the list are equal, says so;
#   otherwise, expects to say whether first number in the list
#   is smaller than or greater than last number.
#
# - Draws a "picture", and expects 2 more "pictures" to be drawn.

from random import seed, randrange
import sys


try: 
    for_seed, length = (int(x) for x in input('Enter two integers, the second '
                                              'one being strictly positive: '
                                             ).split()
                       )
    if length <= 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(for_seed)
values = [randrange(1, 10) for _ in range(length)]
print('Here is the list of generated values:', values)
print()
if values[0] == values[-1]:
    print('The first and last values are equal.')
elif values[0] > values[-1]:
    print('The first value is greater than the last value.')
else:
    print('The first value is smaller than the last value.')
print()
print('Here are the values represented as horizontal bars:')
print()
for e in values:
    print('   ', ' * ' * e)
print()

the_max = max(values)
def draw_long_horizontal_line():
    print('   ' + '-' * (the_max * 3 + 2))

def draw_short_horizontal_line():
    print('   ' + '-' * (the_max * 2 + 1))

print('Here they are again within a frame:')
print()
draw_long_horizontal_line()
for e in values:
    print('   |' + ' * ' * e + '   ' * (the_max - e) + '|')
draw_long_horizontal_line()
print()

print('And now in a grid, this time right aligned:')
print()
draw_short_horizontal_line()
for e in values:
    print('   ' + '| ' * (the_max - e) + '|*' * e + '|')
    draw_short_horizontal_line()
print()
