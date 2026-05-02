from functools import reduce

def find_second_max(acc, x):
    max1, max2 = acc

    if x >= max1:
        return (x, max1)
    elif x > max2:
        return (max1, x)
    return acc

max1, max2 = reduce(find_second_max, [5,4,3,2,5], (float('-inf'), float('-inf')))

print(max2)  # 9