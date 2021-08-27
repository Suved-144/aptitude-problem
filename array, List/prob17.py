#prime no

a = int(input())
count = 0
for i in range(1,a):
    if a % i == 0:
        count = count + 1
    else:
        pass
if count == 1 :
    print(a,"is prime No")
else:
    print(a, "Not a prime no")