class DemoClass:
    def __init__(self, demo):
        self.__demo = demo

    def __add__(self, other):
        return DemoClass(self.__demo + other.__demo)

    def __mul__(self, other):
        return DemoClass(self.__demo * other.__demo)

    def __str__(self):
        return str(self.__demo)


def main():
    # Creating an Object of class Demo and Printing its initialisation value
    obj1 = DemoClass(5)  # Value of Object is being printed by use of overloaded function __str__(self) in DemoClass
    print(obj1)          # Expected output is 5

    obj2 = DemoClass(2)  # Value of Object is being printed by use of overloaded function __str__(self) in DemoClass
    print(obj2)          # Expected output is 2

    addObj = obj1 + obj2  # Addition is possible because of __add__(self , other)
    print(addObj)         # Expected output is 7

    mulObj = obj1 * obj2  # Multiplication is possible because of __mul__(self, other)
    print(mulObj)         # Expected output is 10


if __name__ == '__main__':
    main()
