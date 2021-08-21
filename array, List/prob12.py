a =[-9,15,80,101,4,95,-101]

maax = 0
for i in range(len(a)):
    if a[i]>maax:
        maax = a[i]


miin = 0
for i in range(len(a)):
    if a[i]<miin:
        miin=a[i]

c = maax+miin
print(c)
'''
#https://codewindow.in
#join our telegram channel

n=input()
s=list(map(int, input().split(',')))

maxi=max(s) # finding the maximum number

mini=min(s) # finding the minimum number


print((maxi)+(mini))

# telegram @codewindow
'''