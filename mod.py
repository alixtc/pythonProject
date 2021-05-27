s = 'If comrade Napoleon says so it must be true !'
l = [100, 200, 300]

def foo(arg):
    print(f' arg = {arg}')

class Foo:
    pass

if  __name__=='__main__':
    print(s)
    print(l)
    foo('quux')
    x = Foo()
    print(x)

