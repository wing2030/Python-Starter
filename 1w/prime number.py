number = int(input())
divisor = 1
while (number !=1):
    divisor = divisor+1
    while (number%divisor ==0):
        if (number%divisor == 0):
            print(divisor)
            number = number/divisor
