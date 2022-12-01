# Program to get reverse of each word in a list

l=["Welcome","To","CDAC"]
print("The original list is")
print(l)
n=len(l)

for i in range (n):
    a=l[i]
    b=a[::-1]
    l[i]=b
    
print("The updated list with reversed words is")    
print(l)