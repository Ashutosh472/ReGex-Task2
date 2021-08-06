#TASK 2
#SIRSS2215
#ASHUTOSH KUMAR MISHRA

n=int(input("Enter number of strings to be checked:"))
ls=[]
for i in range(0,n):
  str1=input()
  ls.append(str1)

map1=list(map(lambda in_str:in_str.split(" ")[0], ls))
print(map1)
