#!/usr/bin/python3
add_attribute = __import__('101-add_attribute').add_attribute

class MyClass():
    __slots__ = ['age']

class AnotherClass():
    def __init__(self):
        self.existing_attribute = 42

mc = MyClass()
another_instance = AnotherClass()

# Test 1: Adding an attribute to a class with __slots__
try:
    add_attribute(mc, "age", 30)
    print(mc.age)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

# Test 2: Adding an attribute to a class that already has attributes
try:
    add_attribute(another_instance, "new_attribute", "New")
    print(another_instance.new_attribute)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

# Test 3: Adding an attribute to a function object
def test_function():
    pass

try:
    add_attribute(test_function, "function_attr", "value")
    print(test_function.function_attr)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

# Test 4: Adding an attribute to a tuple (immutable built-in type)
a_tuple = (1, 2, 3)
try:
    add_attribute(a_tuple, "new_attr", 100)
    print(a_tuple.new_attr)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
