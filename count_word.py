str = input("Enter the string:")
c_dict={}
for i in str:
    count = str.count(i)
    c_dict[i] = count
print(c_dict)