print("I'm python . Nice to meet you!")
name = input("enter your name: ")
print("your name is " + name)

if 3 > 2:
    print("yahoo")
else:
    print("Not")

li = []
other_li = [4,5,6]
#append or to add
li.append(1)
li.append(2)
li.append(3)
li.append(4)
li.append(3)

print(li)
#to remove or property
li.pop()
print(li)

li.append(3)
li[4] = 5
print(li)
print(other_li)

print(li[1:3])
print(li[2:])
print(li[:3])
print(li[::2])

# adding & Removing
li.remove(2)
print(li)
#insect etake two argument
li.insert(1,2)
print(li)

print(li.index(2))

t = 1 in li
print(t)

#tuples
tup = (1,2,3,4)
print(tup[0])
tup + (4,5,6,)
print(tup[:2])
print(tup)
y = 2 in tup

#Dictionary store  mappings
empty_dic = {}
filled_dic = {"one":1,"two":2,"three":3,"four":4}
print(filled_dic)
print(filled_dic["one"])
filled_dic.get("one")
print(filled_dic)
filled_dic.setdefault("five",5)
print(filled_dic)

#sets
some_set = set([1,2,2,3,4,5,5])
print(some_set)
filled_set = {1,2,3,4,5}
filled_set.add(6)
other_set = ([3,4,6,8,7,5])
print(other_set)
