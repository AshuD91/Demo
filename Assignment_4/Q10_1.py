# n=int(input("enter the number of words in the sentence "))
i=0
a=[]

while 1>0:
    s=input("enter the word ")
    a.append(s)
    b=input("Enter 0 to end, any key to continue")
    if b=="0":
        break
    else:
        print("continue the sentence")
print(a)
a.sort(key=len,reverse=True)                    # to get descending order based on length

print("The updated list based on length descending order ")
print(a)
