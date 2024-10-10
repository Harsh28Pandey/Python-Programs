def two_sum(a,target):
    i = 0
    j = len(a) - 1
    while(i < j):
        if((a[i] + a[j])==target):
            print(f'{a[i] , a[j]}')
            print(f'{i , j}')
            return True
        elif((a[i] + a[j]) < target):
            i = i + 1
        else:
            j = j - 1
    return False


target = 22
print(two_sum([1,2,11,12,10,15,7,8],target))


# n = int(input("Enter the list:"))
# for i in range(n):
#     a = list(map(int,input().split()))
# target = int(input("Enter the target:"))
# two_sum(n,target)