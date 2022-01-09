def is_odd(x):
    return x % 2 == 0


print(list(filter(is_odd, list(range(10)))))