'''
#just like structure in c 

sabKuch = {
    "name" : "adiba",
    "cgpa" :9.6,
    "marks":[98,87,65],
    "its_ok":True,
    "subject":["python","C","java"],
}

print(sabKuch)

print(sabKuch["name"])

print(type(sabKuch))

print(sabKuch["subject"])

sabKuch["name"] = "naaz" #change the value by this 

print(sabKuch["name"])

'''
'''

student = {
    "name" :"rahul bhai",
    "subject": {
        "phy":98,
        "math":87,
        "science":90
    }
}

print(student)
print(student['subject'])
student.update

'''

def checkOddEven(x):
    if(x % 2 ==0):
        print("Even")
    else:
        print("Odd")
        
        
checkOddEven(3)
