def private_protected(name, *args):
    attributes = args[1]
    buf = {}
    print(dict(attributes))
    for a in attributes:
        print(a)
        if not a.startswith("_"):
            print("Error occurred. "
                  "Only private or protected arguments are allowed")
            continue
        buf[a] = attributes[a]

    print(buf)
    return type(name, *args[0], buf)


class MyThing(metaclass = private_protected):

    cls_atr = 0

    @classmethod
    def cls_meth(cls):
        pass

    def inst_method(self):
        pass

x = MyThing
print(x)

# m_str = tuple(getattr(str, a) for a in dir(str) if not a.startswith('_'))
# for m in m_str:
#     print(m.__name__)
#     try:
#         print(m("Mykyta"))
#     except:
#         print("\t skip")


#Variant 2

class MetaNoPublic(type):

    def __new__(cls, name, parents, attrs):

        nopublic_attr = {}

        for name, val in attrs.items():
            if not name.startswith('_'):
                pass
            else:
                nopublic_attr[name] = val


class NoPublic(metaclass=MetaNoPublic):
    _val = "NIK"
    val = "Nik"

instance = NoPublic()
print(hasattr(instance, "val"))
print(hasattr(instance, "_val"))