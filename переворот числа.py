number = input()
if len(number) == 5:
    print(int(number[::-1]))
elif len(number) > 5:
    number_zero = number[0]
    replace_number = number[1::]
    number = number[0] + replace_number[::-1]
    def r(n): return int(str(n)[0] + str(n)[-1:0:-1]) if len(str(n)) > 5 else int(str(n)[::-1])
    print (int(number))
