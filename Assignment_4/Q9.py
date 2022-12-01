# program to count the number of a word repeated in the list


c=0
l=["hello","hi","greetings","hi","morning","hi"]
n=len(l)

a=input("Enter the word to be found and counted ")

for i in range (n):
    if(l[i]==a):
        print("The word",a,"is found in the list")
        c+=l.count(a)
        print("The word",a,"is repeated",c,"times")
        break
else:
    print("The word",a,"is not found")
    
        




# c=0
# l=["hello","hi","greetings","hi","morning","hi"]
# print(l)
# a=input("enter the word to be found and counted ")

# for i in range (len(l)):
#     if(l[i]==a):
#         c=c+1
# print(" The word",a,"is repeated",c,"times")      