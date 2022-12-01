
#arranging in descending order based on length of the values in a list


l=["Welcome","To","CDAC"]
a=[]
print("The original list is ")
print(l)
l.sort(key=len,reverse=True)
for i in range (len(l)):
    a.append(len(l[i]))
    a.append(l[i])
print("Updated list in descending order of its string length")
print (a)  