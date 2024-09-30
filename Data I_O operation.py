# with open("E:\Practice Programs\Python revision study topic\demo.txt","r") as f:        # read any file through with syntax
#     data = f.read()
#     print(data)
    
# with open("E:\Practice Programs\Python revision study topic\demo.txt", "w") as f:       #overwrite any file through with syntax
#     f.write("new data")
# import os
# os.remove("E:\Practice Programs\Python revision study topic\demo.txt")  #delete any folder 



#LET'S PRACTICE:--->
# with open("practice.txt","r") as f:
#     data = f.read()
    
# newdata = data.replace("python", "java")
# print(newdata)
# with open("practice.txt","w") as f:
#     f.write(newdata)


# def check_for_word():
#     with open("practice.txt","r")as f:
#         data = f.read()
#     word = ("learning")
#     if(data.find(word) != -1):
#         print("found")
#     else:
#         print("not found")
# check_for_word()
    
    
    
# def check_for_line():
#     word = "learning"
#     data = True
#     line_no = 1
#     with open("E:\Practice Programs\practice.txt","r") as f:
#         while data:
#             data = f.readline()
#             if(word in data):
#                 print(line_no)
#                 return
#             line_no += 1
#         else:
#             print("-1")
# check_for_line()

count = 0
# with open("E:\Practice Programs\Python revision study topic\sample.txt","r")as f:
#     data = f.read()
    
#     nums = data.split(",")
#     for val in nums:
#         if(int(val) %2 ==0):
#             count +=1
# print(count)


