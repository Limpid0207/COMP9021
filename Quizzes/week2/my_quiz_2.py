# Written by *** and Eric Martin for COMP9021


from random import seed, randrange
import sys


try:
    for_seed, length, cap, start =\
        (int(x) for x in input('Enter four positive integers: ').split())
    if for_seed < 0 or length < 0 or cap < 0 or start < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(for_seed)
values = [randrange(length) for _ in range(length)]
print('Here is the list of generated values:')
print('  ', values)
print('Here is a reversed copy of the list (why not?):')
print('  ', list(reversed(values)))
if values:
    print('The minimal and maximal values are, respectively,',
          min(values), 'and', f'{max(values)}.'
         )
print('The sum of all values is:', sum(values))
print('Starting from the middle of the list and wrapping around,')
print('the indexes are:')
print('  ', ', '.join(str((len(values) // 2 + i) % len(values))
                          for i in range(len(values))
                     )
     )
print()

# The function modifies the argument L and has no return statement.
# Using pop() is natural.
def remove_values_no_greater_than_index(L):
    i = 0
    while i < len(L):
        if int(L[i]) <= i:
            L.pop(i)
            continue
        i += 1

# The function does not modify the list passed as argument
# and returns a new list.
# Using remove() is natural.
def cap_sum_to(n, L):
    L1 = list(reversed(L))
    while sum(L1) > n:
        L1.remove(max(L1))
    return list(reversed(L1))



# The function does not modify the list passed as argument
# and returns a new list.
# Using append() is natural.
def increasing_sequence_from(n, L):
    if n not in L:
        return []
    L1 = [n]
    current_max = n
    i = L.index(n)
    while i < len(L):
        temp = int(L[i])
        if temp > current_max:
            current_max = temp
            L1.append(current_max)
        i += 1
    i = 0
    while i < L.index(n):
        temp = int(L[i])
        if temp > current_max:
            current_max = temp
            L1.append(current_max)
        i += 1
    return L1




print('In a copy of the list,')
print('removing again and again the leftmost value')
print('not strictly greater than its latest location (index):')
# A copy of the list.
values_1 = list(values)
remove_values_no_greater_than_index(values_1)
print('  ', values_1)
print()
print('In a copy of the list,')
print('removing again and again the rightmost largest value')
print('so the resulting list of values has a sum no greater than',
      f'{cap}:'
     )
print('  ', cap_sum_to(cap, values))
print()
print('In a copy of the list,')
print('starting from the leftmost occurrence of', start,
      'and wrapping around,'
     )
print('collecting again and again the next larger value:')
print('  ', increasing_sequence_from(start, values))
print('The original list has not been modified indeed:')
print('  ', values)