def pallindrome(s):
    i = 0
    j = len(s) - 1
    while(i < j):
        if(s[i] != s[j]):
            return False
        i = i + 1
        j = j - 1
    return True

n = int(input("Enter the number of strings which you want to check:"))
for i in range(n):
    s = str(input("Enter the string:"))
    print(pallindrome(s))