# printing duplicate letter from string
ifPresent = False
a = 'suveds'
a1 = []
for i in range(len(a)-1):
    for j in range(i+1,len(a)):
        if a[i]==a[j]:
            if a[i] in a1:
                break
            else:
                a1.append(a[i])
                ifPresent = True
if (ifPresent):
    print(a1)
else:
    print("NO Duplicate array in list")
str1 = ''
for ele in a1:
    str1+=ele
print(str1)