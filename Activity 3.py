l = [1,5,2,6,8,3,9,21,41,23,4,55,56,65,34,324,312,]
print(f"Original list: ,{l}")

count = 0

for i in l:
    count += i

avg = count / len(l)

print("Sum = ",count)
print("Average = ",avg)

l.sort()

print("The largest value of the list is ", l[-1])
print("The samllest value of the list is ", l[0])