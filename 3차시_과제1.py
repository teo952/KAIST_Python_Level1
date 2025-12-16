numbers = [1, 2, 3, 4, 5, 6]
print("numbers list          = {:<30}".format(str(numbers)))

numbers.append(7)
print("numbers.append(7)     = {:<30}".format(str(numbers)))

numbers[0] = 0
print("numbers[0] = 0        = {:<30}".format(str(numbers)))

numbers.insert(1, 1)
print("numbers.insert(1, 1)  = {:<30}".format(str(numbers)))

del numbers[7]
print("del numbers[7]        = {:<30}".format(str(numbers)))

numbers.reverse()
print("numbers.reverse()     = {:<30}".format(str(numbers)))

numbers.remove(3)
print("numbers.remove(3)     = {:<30}".format(str(numbers)))

numbers.sort()
print("numbers.sort()        = {:<30}".format(str(numbers)))

numbers.pop()
print("numbers.pop()         = {:<30}".format(str(numbers)))