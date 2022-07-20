tup = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
y = [sum(x) / len(x) for x in zip(*tup)]
print(y)

