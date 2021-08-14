#if input = 34 the  output= 7
#if input = 100 the  output= 1

s = input("Enter any no.")
r = [int(a) for a in s]

d = 0
for i in r:
    d = d + i

print(d)

