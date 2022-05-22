Foo = type('Foo', (), {})
x = Foo()
print(x)

Bar = type('Bar', (Foo, ), dict(attr=100, attr1 = 222))
b = Bar()
print(b.attr)


def f(obj):
    print('attr =', obj.attr)


Fo = type(
    'Foo',
    (),
    {
        'attr': 100,
        'attr_val': f
    }
)

f = Fo()
print(f.attr)
print(f.attr_val())