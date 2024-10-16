
# WAP TO ASK THE USER TO ENTER NAMES OF THEIR 3 FAVOURITR MOVIES & STORE THEM IN A LIST:
movies=[]
mov1 = input("enter 1st movie name: ")
mov2 = input("enter 2nd movie name: ")
mov3 = input("enter 3rd movie name: ")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)

print(movies)
print (type(movies))

# WAP TO CHECK IF A LIST CONTAINS A PALINDROME OF ELEMENTS:
list1 = [1,2,3,2,1]
copy_list1 = list1.copy()
copy_list1.reverse()
if(copy_list1 == list1):
    print("palindrome")
else:
    print("not palindrome")

# WAP TO COUNT THE NUMBER OF STUDENTS WITH THE "A" GRADE IN THE FOLLOWING TUPLE ("C","D","A","A","B","B","A"):
grade = ("C","D","A","A","B","B","A")
print(grade.count("C")) 

# STORE THE ABOVE VALUES IN A LIST & SORT THEM FROM "A" TO "D":
grade = ["C","D","A","A","B","B","A"]
grade.sort()
print(grade) 
