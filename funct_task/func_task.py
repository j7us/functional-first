from pymonad.list import ListMonad
from pymonad.maybe import Just
from pymonad.tools import curry


@curry(2)
def add(first, second):
    return first + second

add10 = add(10)

print(Just(5).map(add10))
print(ListMonad(1,2,3).map(add10))
