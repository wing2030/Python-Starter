import math
number = int(input())
squares = [0, 0, 0, 0]
squares[0] = math.floor(math.sqrt(number))
while (squares[0]>squares[1]):
    number1 = number-squares[0]**2
    squares[1] = math.floor(math.sqrt(number1))
    number2 = number1-squares[1]**2
    squares[2] = math.floor(math.sqrt(number2))
    number3 = number2-squares[2]**2
    squares[3] = math.floor(math.sqrt(number3))
    if (number-squares[0]**2-squares[1]**2-squares[2]**2-squares[3]**2 == 0):
        print (squares)
    squares[0] = squares[0]-1