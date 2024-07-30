n = int(input("Please input positive integer N\n"))
number_list = []
for i in range(n):
    number_list.append(int(input("Please input number\n")))
x = int(input("Please input integer x\n"))
index=-1
for i in range(len(number_list)):
    if(number_list[i]==x):
        index=i
if(index!=-1):
    index+=1
print(index)