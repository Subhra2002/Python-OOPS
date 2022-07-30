class Calculator:
    def __init__(self, num):
        self.number = num

    def square(self):
        print(f"the square of the {self.number} is {self.number**2}")

    def squareRoot(self):
        print(f"the squareRoot of the {self.number} is {self.number**0.5}")

    def cube(self):
        print(f"the cube of the {self.number} is {self.number**3}")
    @staticmethod
    def greet():
        print("WLC to the best calculator in the world")


a = Calculator(9)
a.greet()
a.square()
a.squareRoot()
a.cube()