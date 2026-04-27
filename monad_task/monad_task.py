from pymonad.maybe import Just, Nothing

# посадка птиц на левую сторону
to_left = lambda num: lambda x: (
    Nothing
    if abs((x[0] + num) - x[1]) > 4
    else Just((x[0] + num, x[1]))
)

# посадка птиц на правую сторону
to_right = lambda num: lambda x: (
    Nothing
    if abs((x[1] + num) - x[0]) > 4
    else Just((x[0], x[1] + num))
)

# банановая кожура
banana = lambda x: Nothing

# отображение результата
def show(maybe):
    if maybe.is_nothing():
        print('Упал')
        return

    print('Не упал')

show(
    Just((0,0)).bind(to_left(2)).bind(to_right(5)).bind(to_left(-2))  # канатоходец упадёт тут
)

