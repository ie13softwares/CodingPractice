'''
Python lets us overload operators such as + , - and others for various purposes.
This basic demo shows the overloading of +. * and print so that, the attributes of an object can be printed.
To overload an operator, you would require to redefine their corresponding methods. The list is given below:
 ---------------------------------------------------------------------------
 Operators       Method                        Description                 
 ---------------------------------------------------------------------------
   + 	        __add__(self, other)          Addition
   * 	        __mul__(self, other)         Multiplication
   - 	        __sub__(self, other)         Subtraction
   % 	        __mod__(self, other)         Remainder
   / 	        __truediv__(self, other)         Division
   < 	        __lt__(self, other)         Less than
   <= 	       __le__(self, other)         Less than or equal to
   == 	       __eq__(self, other)         Equal to
   != 	       __ne__(self, other)         Not equal to
   > 	        __gt__(self, other)         Greater than
   >= 	       __ge__(self, other)         Greater than or equal to
   [index] 	__getitem__(self, index)         Index operator
   in 	       __contains__(self, value)         Check membership
   len 	      __len__(self)         The number of elements
   str 	      __str__(self)         The string representation  
----------------------------------------------------------------------------
'''

# Run this file by calling <python operatoroverriding.py> from you terminal


class DemoClass:
    'Class overloading various Operators'
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
