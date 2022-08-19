from itertools import repeat, starmap

res = map(int, {'12', '23', '45'})
# [int('12'), int('23'), int('45')]

numbers = [9, 12, 7, 23, 17, 8]
numbers_exped = list(zip(numbers, repeat(3)))
# [(9, 3), (12, 3), (7, 3), (23, 3), (17, 3), (8, 3)]

res = starmap(pow, numbers_exped)
# [pow(9, 3), pow(12, 3), pow(7, 3), pow(23, 3), pow(17, 3), pow(8, 3)]
