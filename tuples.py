tuple1 = 5, 6, 76, 5
list1 = [5, 6, 76, 5]
list1.sort(reverse=True)
print(list1)

new_tuple = tuple(list1)
print(new_tuple)

list1.sort(reverse=False)
print(list1)

print(tuple1.count(5))
print(tuple1[-1])
