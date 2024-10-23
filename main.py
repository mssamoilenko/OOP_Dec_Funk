import datetime
#task1,#task2
def time():
    c_time = datetime.datetime.now().strftime("%H:%M")
    return c_time
def decor(c_time):
    print("*" * 50)
    def decor2(c_time):
        return str(c_time).center(50)
    print(decor2(c_time))
    print("*" * 50)
decor(time())
#task3
def decorator(cls):
    class WrappedClass(cls):
        def showTime(self):
            print("*" * 50)
            result = super().showTime()
            print(result)
            print("*" * 50)
    return WrappedClass
def decorator2(cls):
    class WrappedClass(cls):
        def showTime(self):
            result = super().showTime()
            return str(result).center(50)
    return WrappedClass
@decorator
@decorator2
class Time:
    def __init__(self,time):
        self.time = time
    def showTime(self):
        return self.time

time1 = Time(datetime.datetime.now().strftime("%H:%M"))
time1.showTime()
#task4
class Pizza:
    def __init__(self):
        self.ingredients = []

    def show_ingredients(self):
        return f"Pizza with: {', '.join(self.ingredients)}"

def add_ing(ingredient):
    def decorator(func):
        def wrapper(pizza):
            pizza.ingredients.append(ingredient)
            return func(pizza)
        return wrapper
    return decorator

@add_ing("tomato")
@add_ing("mozzarella")
def margherita(pizza):
    return pizza.show_ingredients()

@add_ing("tomato")
@add_ing("mozzarella")
@add_ing("gorgonzola")
@add_ing("parmesan")
def quattro_formaggi(pizza):
    return pizza.show_ingredients()

@add_ing("tomato")
@add_ing("mozzarella")
@add_ing("ham")
@add_ing("mushrooms")
@add_ing("artichokes")
def capricciosa(pizza):
    return pizza.show_ingredients()

@add_ing("tomato")
@add_ing("mozzarella")
@add_ing("ham")
@add_ing("pineapple")
def hawaiian(pizza):
    return pizza.show_ingredients()

pizza1 = Pizza()
print(margherita(pizza1))
pizza2 = Pizza()
print(quattro_formaggi(pizza2))
pizza3 = Pizza()
print(capricciosa(pizza3))
pizza4 = Pizza()
print(hawaiian(pizza4))
