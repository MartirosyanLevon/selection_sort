a = [2,2,-1,-5,55,66,34,0,10,-66]
n = len(a)

print(a)

for i in range(n-1):
    for j in range(i+1,n):
        if a[i] > a[j]:
            a[i],a[j] = a[j],a[i]

print(a)
