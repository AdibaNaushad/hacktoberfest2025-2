# control statment 
'''
condition - if , elif ,else
for while else suite
nested
infinite loop
pass
continue
break
assert return

#systax
if - age = int(input(enter)) # for space we give is said indentation 
     if age >= 18:
      print('you can vote)


      '''
'''age = int(input('enter  = '))
if age >= 18:
      print('you can vote')
else:
        print('cannot')


mark = int(input('Enter mark'))
if mark >=90 and mark < 100:
    print('A+')
    print('pass')
elif  mark <=35:
        print('fail')    

loop----
while loop : systax
       while condition :
        

        i = 1
while i <=5 or i >= 10:
  print(i)
  i += 1


        '''''

    
'''for loop :

a=[1,2,3,4,5]
for i in a:
  print(i)

for i in range(1,20):
    print(i)

    '''


'''i = 1
while i <=5 or i >= 10:
  print(i)
  i += 1
  '''


''' a=[1,2,3,4,5]
for i in a:
  print(i)

for i in range(1,20):
    print(i)
    '''


'''infinity loop

 while True:
    print(1)
    
    '''


#range(start,stop,step) 
''' 
start -1
stop- 100
step-1

sytax-->

a = list(range(1,11,1))
print(a)


a = tuple(range(1,10,1))
print(a)



'''

'''a = list(range(1,10,1))
print(a)

a = tuple(range(1,10,1))
print(a)'''

'''#nested loop

i = 1
j = 2
for i in range(1,3):
  for j in range(2,5):
     print(f'{i},{j}')

'''

'''

for i in range(1,3):
  for j in range(2,5):
     print(f'{i},{j}')

'''

'''

a = int(input("Enter a : "))
b = int(input("Enter age b : "))
c = int(input("Enter c : "))



if (a < b):
  if(b < c):
    print("c is big")
  elif(b>c):
    print("b is big")
else:
  print("a is big")
'''














n = 3

def pos(n):
    if(n>0):
        while(n>0):
         print(n,end=" ")
         n-=1



def neg(n):
    if(n<0):
        while(n<0):
          print(n,end=" ")
          n+=1
    