#arranging in descending order based on length of the values in a list

l=["Welcome","To","CDAC"]
a=[]
print("The original list is")
print(l)
l.sort(key=len,reverse=True)
for i in range (len(l)):
    a.append(str(len(l[i]))+ "="+ l[i])
print("Descending order of the given list")    
    
print(a)