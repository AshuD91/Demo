# Program for changing of the datatypes
#Syntax- var1=datatype(var2)

# integer type to other datatypes

a= 10
print("original type",type(a))

print("changed type",str(a))            #integer value changes to string value
b=str(a)
print("changed type",type(b))           #integer datatype changes to string datype

print("changed type",float(a))          #integer value changes to float value
c=float(a)
print("changed type",type(c))           #integer datatype changes to float datype

print("changed type",complex(a))        #integer value changes to complex value
d=complex(a)
print("changed type",type(d))           #integer datatype changes to complex datype

print("changed type",bool(a))           #integer value changes to boolean value
e=bool(a)
print("changed type",type(e))           #integer datatype changes to boolean datype



# string type to other datatypes is not possible

a= "Ashutosh"
print("original type",type(a))


print("changed type",bool(a))           #string value changes to boolean value
b=bool(a)
print("changed type",type(b))           #string datatype changes to boolean datype




# float type to other datatypes


a= 10.0
print("original type",type(a))


print("changed type",int(a))           #float value changes to integer value
b=int(a)
print("changed type",type(b))          #float datatype changes to integer datype


print("changed type",str(a))           #float value changes to string value
c=str(a)
print("changed type",type(c))          #float datatype changes to string datype


print("changed type",complex(a))        #float value changes to complex value
d=complex(a)
print("changed type",type(d))           #float datatype changes to complex datype


print("changed type",bool(a))           #float value changes to boolean value
e=bool(a)
print("changed type",type(e))           #float datatype changes to boolean datype



# complex type to other datatypes
a=10j
 
print("original type",type(a))

print("changed type",str(a))           #complex value changes to string value
b=str(a)
print("changed type",type(b))          #complex datatype changes to string datype


print("changed type",bool(a))           #complex value changes to boolean value
c=bool(a)
print("changed type",type(c))           #complex datatype changes to boolean datype







