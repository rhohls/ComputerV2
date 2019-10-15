def squareRoot(number, precision):
    start = 0
    end = number
    ans = 0

    # integer
    while start <= end:
        mid = int((start + end) / 2)

        if mid * mid == number:
            ans = mid
            break

        if mid * mid < number:
            start = mid + 1
            ans = mid
        else:
            end = mid - 1

    # float (precision)
    increment = 0.1
    for i in range(0, precision):
        while ans * ans <= number:
            ans += increment

        ans = ans - increment
        increment = increment / 10

    return ans


def square(number):
    return number * number


def custom_power(number, power):
    i = 1
    if power == 0:
        return 1
    while i < power:
        number *= number
        i += 1
    return number

def operation(num1, num2, operand):
    if operand == '+':
        return (num1 + num2)
    elif operand == '-':
        return (num1 - num2)
    elif operand == '*':
        return (num1 * num2)
    elif operand == '/':
        return (num1 / num2)
    elif operand == '%':
        return (num1 % num2)
    elif operand == '^':
        return custom_power(num1, num2)
    else:
        raise Exception ("opperand doesnt exist")