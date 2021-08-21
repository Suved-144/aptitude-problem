#Given three numbers b, e and m. Fill in a function that takes these three positive integer values and outputs b^e mod m.

a = int(input())
b = int(input())
c = int(input())
d = (a**b)%c
print(d)