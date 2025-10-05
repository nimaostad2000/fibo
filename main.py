def fib(number: int):
    if number <=1:
        return number
    else:
        return fib(number-1)+fib(number-2)
number = 6
result = fib(number)
print(f"fib({number}) = {result}")