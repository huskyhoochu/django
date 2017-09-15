def double(*args):
    if len(args) == 1:
        return args[0] ** 2
    elif len(args) == 2:
        return args[0] * args[1]

double(3,5)
