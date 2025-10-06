def factorial(number: int):
    if number == 1:
        return 1
    return number * factorial(number - 1)
number = 6
print(factorial(number))
#git init
# git status
# git add --all
# git commit -m "meaningfull message"