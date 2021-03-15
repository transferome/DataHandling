"""  Module  """
import scopes.manynames as manynames


x = 66


def f():
    x = 100
    print(x)

x
manynames.x
f()
manynames.g()
