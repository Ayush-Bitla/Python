users = ['Ayush','Sakshi','Gurav']

data = ['Ayush',20,True]

emptylist = []

print("Ayush" in emptylist)

print(users[0])
print(users[-2])

print(users.index('Sakshi'))

print(users[0:2])
print(users[1:])
print(users[-3:-1])

print(len(data))

users.append('Dikshita')
print(users)

users += ['Shivam']
print(users)

users.extend(['Vinay','Dhruv'])
print(users)

# users.extend(data)
# print(users)

users.insert(0, 'Akshay')
print(users)

users[2:2] = ['Arya','Rishi']
print(users)

users[1:3] = ['Rohan','BJP']
print(users)

users.remove('BJP')
print(users)

print(users.pop())
print(users)

del users[0]
print(users)

# del data
data.clear()
print(data)

users[1:2] = ['Ayush']
users.sort()
print(users)

users.sort(key=str.lower)
print(users)

nums = [4, 42, 78, 1, 5]
nums.reverse()
print(nums)

# nums.sort(reverse=True)
# print(nums)

print(sorted(nums, reverse=True))
print(nums)

numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(numscopy)
print(mynums)
mycopy.sort()
print(mycopy)
print(nums)

print(type(nums))

mylist = list([1, "Sakshi", True])
print(mylist)

# Tuples

mytuple = tuple(('Ayush', 42, True))

anothertuple = (1, 4, 2, 8, 2, 2)

print(mytuple)
print(type(mytuple))
print(type(anothertuple))

newlist = list(mytuple)
newlist.append('Om')
newtuple = tuple(newlist)
print(newtuple)

(one, *two, hey) = anothertuple
print(one)
print(two)
print(hey)

print(anothertuple.count(2))
