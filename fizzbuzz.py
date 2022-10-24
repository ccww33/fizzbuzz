import math
from decimal import Decimal


def isFizzBuzz():
     for index in range(1, 100):
         #if type(Decimal(index / 3)) == int:

         if float(index / 3) == int(index / 3) and float(index / 5) == int(index / 5):
             print(str(index), "FizzBuzz", "Multiple by", str(int(index / 3)), "and", str(int(index / 5)))

         if float(index / 3) == int(index / 3):
             print(str(index), "Fizz", "Multiple by", str(int(index / 3)))

         if float(index / 5) == int(index / 5):
             print(str(index), "Buzz", "Multiple by", str(int(index / 5)))

         else:
             print(index)

isFizzBuzz()





