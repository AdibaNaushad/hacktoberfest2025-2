# with open("sample.txt","r") as f:  #no need to close 
    #  data = f.read()
    #  print(data)


#  to delect file 
# import os
# 
# os.remove("sample.txt")
# 



# with open("sample.txt","w") as f:  #no need to close 
    # data = f.write("hello")
    # print(data)


# #replace a word 
# with open("sample.txt","r") as f:  #no need to close 
#      data = f.read()

#      new_data = data.replace("java","Python")
#      print(new_data)

#find word
# def checkWord():
    # word = "java"
    # with open("sample.txt","r") as f:  #no need to close 
        #    data = f.read()
        #    if(data.find(word) != -1):
                # print("found")
        #    else:
                # print("not fouund")
# 
# checkWord()



# def checkLine():
    #   word = "java"
    #   data = True
    #   line_no = 1
    #   with open("sample.txt","r") as f:  #no need to close 
        # data = f.read()
        # if(word in data):
            #  print(line_no)
            #  return
            #  line_no+=1
        # return -1
# 
# checkLine()
# print(checkLine())

count=0
with open("practice.txt","r") as f: 
       data = f.read()
       print(data)
        
       num = data.split(",")
       for val in num :
              if(int(val)%2 == 0):
                count+=1 

print(count)
    #    num = ""
    #    for i in range (len(data)):
    #      if(data[i] == ","):
    #            print(num)
    #      else:
    #           num += data[i]
    # 
   
   
   
   
   