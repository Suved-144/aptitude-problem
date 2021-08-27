a = int(input())

sum1 = 0
for i in range(1,a):
    if a % i == 0:
        sum1 = sum1 + i
    else:
        pass

if sum1 == a:
    print(a ," is  a  Perfect no ")
else:
    print("Not a perfect no")