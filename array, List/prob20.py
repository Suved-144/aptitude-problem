#Move all the negative elements to one side of the array


a = [-1, 2, -3, 4, 5, 6, -7, 8, 9]
j = 0
for i in range(len(a)):
    if a[i]<0:
        temp = a[i]
        a[i] = a[j]
        a[j] = temp
        j = j+1

print(a)