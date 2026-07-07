arr = [1,2,3,4]
t = 5
if arr[0]+arr[1]==t:
    print([0,1])
n =len(arr)

for i in range(2,n):
    for j in range(0,i):
        if arr[i]+arr[j]==t:
            print([j,i])