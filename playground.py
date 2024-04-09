def add(*args):
    suma = 0
    for i in args:
        suma+=i
    print(suma)
add(5,4,6,4)

def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items()>
    # print(key)
    # print(value)
    n+=kwargs["add"]
    n*=kwargs["multiply"]
    print(n)
calculate(2,add=3,multiply=5)

class Car:

    def __init__(self, **kw) -> None:
        self.make = kw["make"]
        self.model = kw["model"]
my_car = Car(make="Nissan", model = "GT-8")
print(my_car.model)