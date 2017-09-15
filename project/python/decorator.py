def print_debug(func):
    def inner_func(*args, **kwargs):
        print('args:', args)
        print('kwargs:', kwargs)
        return func(*args, **kwargs)
    return inner_func

@print_debug
def any_func(a, b):
    return a * b

any_func(3, 5)

@print_debug
def kwargs_func(name, age, gender):
    return {'name':name, 'age': age, 'gender': gender}

kwargs_func(name='hyung soo',age='27',gender='male')
