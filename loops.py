items = [1, 2, 3, 4, "hi"]

item_len = len(items)

print(item_len)

# how to do a for loop in python

#to print the items inside the list
for i in items:
print(i)

#range(start, stop, step)
for i in range(0, 3, 3):
    print(items[i])

items = [100, 200, 300, 400, 500, 600, 700]
my_range = range(len(items))
print(my_range)

for i in range(len(items), 2):
    print(items[i])


items = [200, 300, 400, 500, 600, 700, 800, 900, 1000]

for i in range(0,len(items)-1,2):
    print(items[i])
