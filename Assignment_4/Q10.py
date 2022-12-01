# Program to get word with longest length in a given sentence
# a=[]
# while (1):
#     s=input("enter the word ")
#     if(s=="end"):
#        exit
#     else:
#         a.append(s)
# print(a)



# 
n=int(input("enter the number of words in the sentence "))
i=0
a=[]

while i<n:
    s=input("enter the word ")
    a.append(s)
    i+=1

  
print(a)
a.sort(key=len,reverse=True)                    # to get descending order based on length

print("The updated list based on length descending order ")
print(a)

print("word with longest length in the given list is ",a[0])



