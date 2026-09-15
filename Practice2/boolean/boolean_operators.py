x = 200
print(isinstance(x, int))
print(isinstance(x, str))

a = 100
b = 50
if a > b:
    print("a is greater than b")
else:
    print("a is not greater than b")

def is_student():
    return True
print(is_student())

def is_adult():
    return True
if is_adult():
    print("You are an adult")
else:
    print("You are not an adult")
