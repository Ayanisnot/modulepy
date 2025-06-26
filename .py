mylist = [3, 4, 5, 7, 1, 9]
print("original list : " , mylist)

count = 0

for i in mylist:
    count = count + i

avg = count/len(mylist)

print("sum :" , count)
print("average :" , avg)
print()

mylist.sort()
print(mylist)

print("small element is " , mylist[0])