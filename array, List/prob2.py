a = [4, 6 ,9, 7, 5,3 ]
#print(max(a))
#print(min(a))
maxx =0
minx = 0
for i in range(len(a)):
    if a[i]>maxx:
        maxx = a[i]

    #if a[i]<minx:
     #   minx = a[i]


print(maxx)
#print(minx)
for i in range(len(a)):
    if a[i]<minx:
        minx = a[i]

    #if a[i]<minx:
     #   minx = a[i]
print(minx)