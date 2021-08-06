def is_prime(n):
  for i in range(2,n):
    if n%i==0:
      return False
  else:
    return True

#Function to find the list of prime numbers till num
def prime_list(num):
  list_prime=[]
  for i in range(2,num):
    if (is_prime(i)):
      list_prime.append(i)
  return list_prime

r=int(input("Enter a number:"))
list1=prime_list(r)
o=[]
for k in list1:
  if r%k==0:
    o.append(k)

print(f"Prime factors of {r} are {o}")
