class Tripletone(type):

    limit = 3
    counter_new = 0
    clues = ("first", "second", "third")
    clues_dict = {"first": None, "second": None, "third": None}

    def __new__(cls, name, parents, attrs):

        if cls.limit:
            cls.limit -= 1
            res = cls.clues_dict[cls.clues[cls.counter_new]] = \
                super(Tripletone, cls).__new__(cls, name, parents, attrs)
            cls.counter_new += 1
            return res

        elif name in cls.clues:

            if instance := cls.clues_dict.get(name, None):
                # print(instance)
                del instance
                res = cls.clues_dict[name] = \
                    super(Tripletone, cls).__new__(cls, name, parents, attrs)
                return res

        else:
            raise ValueError("Too many instances")



    # def __call__(self, *args, **kwargs):
    #     self.__class__.counter_new += 1
    #     return super(Tripletone, self).__call__(self, *args, **kwargs)


class A(metaclass=Tripletone):
    pass


class B(metaclass=Tripletone):
    pass


class C(metaclass=Tripletone):
    pass


# class D(metaclass=Tripletone):
#     pass


class first(metaclass=Tripletone):
    pass


print(Tripletone.counter_new)
print(Tripletone.limit)
print(Tripletone.clues_dict)
print(A)

