def recurse(number):
    if number < 5:
        return number
    print(number)
    return recurse(number-1)

print(recurse(10))