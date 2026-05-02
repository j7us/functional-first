from pymonad.tools import curry
from pymonad.list import ListMonad
from pymonad.state import State


@curry(3)
def cells_around(N, M, coord):
    x, y = coord
    result = []

    if 1 <= x <= N and 1 <= y <= M:
        result.append((x, y))

    if 1 <= x <= N and 1 <= y - 1 <= M:
        result.append((x, y - 1))

    if 1 <= x + 1 <= N and 1 <= y <= M:
        result.append((x + 1, y))

    if 1 <= x - 1 <= N and 1 <= y <= M:
        result.append((x - 1, y))

    if 1 <= x <= N and 1 <= y + 1 <= M:
        result.append((x, y + 1))

    return ListMonad(*result)


@curry(3)
def perform_capture(N, M, captured_points):
    def inner(days):
        if N * M == len(captured_points):
            return days + 1, captured_points

        updated_points = set(ListMonad(*captured_points).bind(cells_around(N, M)))

        return perform_capture(N, M, updated_points).run(days + 1)

    return State(inner)


def conquest_campaign(N, M, L, battalion):
    captured_points = set(zip(battalion[::2], battalion[1::2]))

    res = State.insert(captured_points).then(perform_capture(N, M))

    count, capt = res.run(0)

    return count


print(conquest_campaign(3, 4, 2, [2, 2, 3, 4]))
