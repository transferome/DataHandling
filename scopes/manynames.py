"""  Showing how python handles the assignment of names to objects
 within 'namespaces' """

# Global (module) - name/attribute (X or manynames.X)
x = 11


def f():
    # accesses global x
    print(x)


def g():
    # local x declared, masks global x
    x = 22
    print(x)


class C:
    # class attribute C.x
    x = 33

    def m(self):
        # local x assigned within method
        self.x = 55
        x = 25
        # local x returned along with the instance attribute
        print(self.x, x)


if __name__ == '__main__':
    print(x)
    f()
    g()
    print(x)

    # makes instance
    obj = C()
    obj.x
    obj.m(5)
    obj.x
    obj1 = C()
    obj1.m(10)
    obj1.x
    obj2 = C()
    obj2.x
    # class name inherited by instance
    print(obj.x)

    # calls method, now obj.x changes, however C.x does not
    obj.m()
    print(obj.x)
    print(C.x)

    # print(C.m.x)
    # print(g.x)
