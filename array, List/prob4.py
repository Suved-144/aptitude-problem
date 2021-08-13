#printing Non repeating element in strin
a = 'ssuuvved'
b =[]
count = 0
counts = 0
for i in range(len(a)):
    for j in range(len(a)):
        if a[i]==a[j]:
            count+=1
        else:
            counts+=1

    if count==1 and count>=1:
        b.append(a[i])
        count = 0
        counts = 0
    else:
        count = 0
        counts = 0

#print(b)
str1 = ''
for ele in b:
    str1+=ele

print(str1)
print(len(str1))