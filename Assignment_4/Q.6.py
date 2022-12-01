                    #list methods
#lets us consider a single list as an example to describe following methods

l=["Ashutosh","Arnab","Amaljith","Kunal","Pavan","Sanket","Shivang","Sourabh","Vishal"]


#append()-it is a function used to join additional string to a list.
#          but the added string or value is added at last place.
# Syntax=  list.append(value)

          

# lets add something or any value to the list L , add "CDAC"
l.append("CDAC")
print(l)


#extend()-it is a function used to join two lists to one of the list.
#          but the added list or values are added after the values of first list.
#          follwoing syntax add l2 values to l1
# Syntax=  list1.extend(list2)

            # l2 list is just a new list to store the updated list
l2=l
            # lets create another list L3
l3=["CDAC","KOLKATA"]

            #add l3 to l2 so that l2 is extended with the values from l3
l2.extend(l3)
print("updated l2 list is")
print(l2)
print("l3 is not updated")
print(l3)     #l3 remain same but l2 is extended

              #if we do it alternately
l3.extend(l2) #l2 values (updated) are added to l3
print("updated l3 list is")
print(l3)


# insert()- its a function used to insert a value in the list.
#           the values can be inserted at a specific valid location in the list. 
#           the added value takes the position and other value's positions are updated.
#           its snytax uses two arguements.
# Syntax= list.insert(position,value)           

        

# lets say we add "2022" between Pavan and Sanket 
# the location in lists start from 0 to n-1, where n is the length of list
# so we need to add 2022 at position 5.

l.insert(5,"2022")  
print("the updated list l is")
print(l)



# index()-its a method used to return the position of the value needed.
#         it only gets the position of first value, 
#         in case of multiple elements having same Values.
# Syntax - list.index(value)

        

# lets say we need the position of element with value kunal. 
# the location in lists start from 0 to n-1, where n is the length of list.
# the location will be one less. we may need variable to store the value of position

p=l.index("Kunal")  
print("The position of element with value Kunal in the list L is ") 
print(p)         
            

#sort()-its a function used to sort the element in increasing or decreasing values.
#Syntax-list.sort()

l.sort()    # since values are strings and one int, the y are arranged in  int, A_Z order
print(l)
