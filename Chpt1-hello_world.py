message = "Hello Python world!"
print(message)

message = "Hello Python Crash Course world!"
print(message)

print(5+3)
print(9-1)
print(16/2)
print(4*2)

bicycles=['trek','cannondale','redline','huffy']

print(bicycles[3].title())

bicycles.append('ducati')

bicycles.insert(0,'jixxer')

print (bicycles)

popped_bicycles = bicycles.pop()

print (bicycles)

danger = 'jixxer'
bicycles.remove(danger)
print (bicycles)

print('\nA {danger.title()} is too dangerous for me.')

import sys
print(sys.executable)