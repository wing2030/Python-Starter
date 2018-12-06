mod_number = int(input())
basic_list = list(range(mod_number))
key_list = list(range(mod_number))
gcd = mod_number
for number in basic_list:
    key_list[number] = mod_number//(basic_list[number]+1)
for number1 in basic_list[1:]:
    for number2 in basic_list[number1:]:
        for number3 in basic_list[:number2-1:-1]:
            if (((number3+1)%(number1+1) == 0) & ((number3+1)%(number2+1) == 0)):
                gcd = number3
        if (key_list[number1]*key_list[number2]/mod_number == key_list[gcd]):
            print(number1+1, number2+1)
print(basic_list)
print(key_list)