marks=[5,6,8,3,4,5,"harry"]
# print(marks)
# print(marks[0])
# print(type(marks))

# negative index
print(marks[-3])
print(marks[len(marks)-3])
print(6-3)
print(marks[3])




# finding in list 
if 5 in marks:
    print("yes")
else:
    print("no")


if "arry" in "harry":
    print("yes")


print(marks)
print(marks[:])
print(marks[1:-1])        # nagative indexing technique using
print(marks[1:6]) # same as above 
# jump index
print(marks[1:4:2])












# list comprehension
lst=[i for i in range(4)]
print(lst)
# list comprehension
lst=[i for i in range(10) if i%2==0]
print(lst)




# list methods
l=[4,45,7,6,5,43,5]
l.append(5)
l.sort()
l.sort(reverse=True)
l.reverse()
l.index(4)
k=l.count(4)
l.copy()
m=l.copy()
m[0]=0
print(l)