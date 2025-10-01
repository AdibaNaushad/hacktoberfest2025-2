'''

marks =[94.4,98.67,56.7,90.54] #can change or re-assign value (motiable)
print(marks)
print(marks[3])
print(len(marks))


student = ["adiba",98.45,"asansol"]
student[0]="arjun"
print(student)

student = ['adiba',98.65,'delhi',98.56]
print(student[-3:-1])


'''
'''

#list.append() ----- add in end 

student = ["adiba",98.45,"asansol"]
student.append(4)
print(student)

'''
'''

list=[1,2,3,4]


list.append(4) #add in end of list 
print(list)

list.sort() #arrange in assending order
print(list)

list.reverse() #reverse the num 
print(list)

list.insert(3,6) #insert in (excahnge-position , the num which will insert)
print(list)

list.remove(4) # just remove present num
print(list)

list.pop(2) #index 2 postion number will be remove 
print(list)

'''

#tuples (immutable can not change element )

tuple = (5,6,6,7,3) 
print(tuple)
print(type(tuple))

#print(tuple[0:1]) #slicing 

#print(tuple.index(2))
movie = []

a = input("enter name 1 : ")
b = input("enter name 2 : ")
c = input("enter name 3 : ")

movie.append(a)
movie.append(b)
movie.append(c)

print(movie)









