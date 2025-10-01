''' the rule py follo is called "PEMDAS"
parantaciss ()
exponanial 'e'
multilpe X
div "/"
add + 
sub -
'''
result = 10+2+5
print(result)

#arthmatic operater
x = 10
y = 3
print(x+y)
print(x-y)
print(x*y)
print(x/y) #div
print(x//y) # floor div ( ans will be depend on variable ans will be integer for both x,y but float then ans will be float
print(x%y)#remainder
print(x**y) #power

#comparation operater
print(x == y)
print(x != y)
print(x >= y)
print(x <= y)

#logical operater 
age = 20
its_student = True

print(age>18 and its_student) #and
print(age > 25 or its_student) #or
print(not its_student) #not

#assingment operater (=, += ,-= ,*=,)

#identity operater ,compare object the  memory location  of variable  (is > True , is not  )

a = [1,2,3]
b = a
c = [1,2,3]
print(a is b) #true
print(a is  not b) #false
print(a is c) #false
print(a is not c) #true

#membership 
# the given variable is present in it or not by using  (in , in not )

veg =['kerela','aloo','tomato']
print("kerela" in veg)
print("bindi" in  veg)


#prblm 1 ) write area of circle 
pie = 3.14
radius = float(input("Enter radius = "))

area_circle = pie*radius*radius
print(f"the area is: {area_circle}")

circumference = 2*pie*radius
print(f'the circumferece is : {circumference}')





















