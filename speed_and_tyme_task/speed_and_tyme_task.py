from functools import reduce

from pymonad.operators.maybe import Just
from pymonad.tools import curry


def to_times(t):
    return [(0, t[0])] + list(zip(t[:-1], t[1:]))

def to_executed_time(t):
    return map(lambda x: x[1] - x[0], t)

@curry(2)
def multiply_with_speed(s, t):
    return list(map(lambda x: x[0] * x[1], zip(s, t)))



lst = [15,1,25,2,30,3,10,5]
tim = lst[1::2]
spd = lst[0::2]

res_by_times = Just(tim).map(to_times).map(to_executed_time).map(multiply_with_speed(spd)).value

res = reduce(lambda x, y: x + y, res_by_times)

print(res)
