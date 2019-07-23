some_var = 5
if some_var > 10:
    print('some_var is smaller than 10')
elif some_var < 10:
    print("some_var is less than 10")
else:
    print("some_var is needed")

print("dog " is "a mammal")
print("cat" is "a mammal")
print("mouse " is "a mammal")

for animal in ["dog","cat","mouse"]:
    print("{0} is a mammal".format(animal))

for i in range(4):
    print(i)

for i in range(4,8):
    print(i)

'''x = 0
while x < 4:
    print(x)
    x += 1
'''
def add(x,y):
    print("x is {0} and y is {1}".format(x,y))
    return x + y
add(5,6)

def keyword_args(**kwargs):
    return kwargs

keyword_args(big="foot", loch="ness")

x = 5
def sex_x(num):
    x = num
print(x)
