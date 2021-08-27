#Find the Union and Intersection of the two sorted arrays.
a = [1, 3, 4, 5, 7]

b = [2, 3, 5, 6]
'''
m = len(a)
n = len(b)
i = 0
j = 0
while i < m and j < n:
    if a[i] < b[j]:
        i += 1
    elif b[j]  < a[i]:
		j+= 1
	else:
		print(b[j])
		j += 1
		i += 1
print(b)
'''
s = set.intersection(set(a), set(b))
t = list(s)
print(t)
s = set.union(set(a),set(b))
print(list(s))