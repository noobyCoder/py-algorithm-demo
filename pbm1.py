# -*- coding: utf-8 -*-
#!/usr/bin/python3



# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.
#answer = 233168


def multipleNum(max, arg1, arg2):
    sum = 0
    for x in range(max):
        if (x % arg1) == 0 or (x % arg2) == 0:
            print(x)
            sum = sum + x
    return sum

sum = multipleNum(10, 3, 5)
print('sum=%s' % sum)
sum = multipleNum(1000, 3, 5)
print('sum=%s' % sum)