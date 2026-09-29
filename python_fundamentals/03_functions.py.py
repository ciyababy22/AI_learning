def square(x):
    return x * x

numbers = [1,2,3,4,5]
result = [square(n) for n in numbers]

print(result)