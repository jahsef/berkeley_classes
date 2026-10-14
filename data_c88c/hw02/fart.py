
my_og = print
my_og(f'actual og: {id(print)}')

def new_print(print):
 """Return a better print that returns its argument"""
 def f(x):
    my_og(f'new_prints f({x})')
    my_og(f'inside print mem: {id(print)}')
    value = print(x)
    
    if value != None:
        return print('What?')
    return x
 return f

og = print

print = new_print(print)
my_og(f'new print 1: {id(print)}')

print = new_print(print)
my_og(f'new print 2: {id(print)}')

my_og('----'*30)
og('print returned', print(2))


