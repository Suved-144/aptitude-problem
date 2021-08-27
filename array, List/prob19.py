#Find the "Kth" max and min element of an array
k = int(input("Enter the value of K"))

s = [13 ,5,6,9,7,25,34]
for i in range(len(s)):
    for j in range(i+1,len(s)):
        if s[i]<s[j]:
            
            temp = s[i]
            s[i] = s[j]
            s[j] = temp


print(s)
print(s[k-1])