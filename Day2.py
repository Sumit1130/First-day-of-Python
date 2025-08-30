#============string========================
# str1 = "This is a string"
# str2 = 'This is a string'
# str3 = """This is a string"""

# str1 = "This is a string. \nIt is used in python" #(\n)It breaks a line.
# str2 = "This is a string. \tIt is used in python"#(\t)it is a tab
# print(f"{str1}")
# print(f"{str2}")

#==========concantentation============
# str1 = "Sumit"
# str2 = "Nepal"
# print(f"{str1 + str2}")

#==========length of string========
# str1 = "My name is Sumit Nepal"
# len1 = len(str1)
# print(f"{len1}")

#==========indexing=========
# str1 = "Sumit Nepal"
# ch = str1[4]
# print(f"{ch}")

#======slicing==========
# str = "sumit nepal"
# print(str[0:13])
# print(str[0:len(str)])

#=====negative index=========
# str = "sumit"
# print(str[-5:-1])



# str = "my name is sumit nepal"
# print(str.endswith("al"))

# str = "my name is sumit nepal"
# str = str.capitalize()
# print(str)

# str = "my name is sumit nepal"
# print(str.replace("i", "s"))

# str = "my name is sumit nepal"
# print(str.find("s"))

# str = "my name is sumit nepal"
# print(str.count("name"))

#=======practice question=============##
# name = input("Enter your name: ")
# print(f"your name length, {len(name)}")

# str = "my name is $ i am basically from $"
# print(str.count("$"))

#============conditional statement===================
# age = 18
# if(age >= 18):
#     print(f"you are eligible for vote")
#     print(f"you are not eligible for vote")

#======traffic light=========
# light = "green"

# if(light == "red"):
#     print("stop")
# elif(light == "green" ):
#     print("go")
# elif(light == "yellow"):
#     print("look & go")
# else:
#     print(f"road is danger!!")

#=======Traffic light from user=======
# light = input("Enter your traffic light:  ").lower()

# if light == "green":
#     print(f"Go")
# elif light == "red":
#     print(f"Stop")
# elif light == "yellow":
#     print(f"Look and Go")
# else:
#     print(f"Road is danger")

#========voter========== 
# age = int(input("Enter your age: "))

# if(age >= 18):
#     print(f"you are eligible for vote")
# else:
#     print(f"you are not eligible for vote")


#==========grade sheet=============
# Marks = int(input("Enter your exam marks:  "))

# if(Marks >= 90):
#     print(f"Congratulations!! your GPA is 4.0")
# elif(90> Marks >= 80):
#     print(f"Congratulations!! your GPA is 3.60")
# elif(80> Marks >= 70):
#     print(f"Congratulations!! your GPA is 3.20")
# elif(70> Marks >= 60):
#     print(f"Congratulations!! your GPA is 2.80")
# elif(60> Marks >= 50):
#     print(f"Congratulations!! your GPA is 2.40")
# elif(50> Marks >= 40):
#     print(f"Congratulations!! your GPA is 2.00")
# elif(40> Marks >= 20):
#     print(f"Better luck for next time!! your GPA is 1.60")

# else:
#     print(f"Sorry!! Better luck for next time ")

#==========another way also============
# marks = int(input("Enter your marks:  "))

# if(marks >= 90):
#     grade = "A+"
# elif(marks >= 80 and marks <90):
#     grade = "A"
# elif(marks >= 70 and marks < 80):
#     grade = "B+"
# elif(marks >= 60 and marks < 70):
#     grade = "B"
# elif(marks >= 50 and marks < 60):
#     grade = "C+"
# elif(marks >= 40 and marks < 50):
#     grade = "C"
# elif(marks >= 30 and marks < 40):
#     grade = "D+"
# elif(marks >= 20 and marks < 30):
#     grade = "D"
# elif(marks >= 0 and marks < 20):
#     grade = "E"
# else:
#     "Error!!!"
# print(f"your grade is: {grade}")




#========nesting===========
# age = int(input("Enter your age:  "))
# if(age >= 18):
#     if(age >= 80):
#         print("Can not drive")
#     else:
#         print("can drive")
# else:
#     print("can not drive")

#========practice question============
#check if a number entered by user is odd or even

# num = int(input("Enter your number: "))

# if(num % 2 == 0):
#     print("Even")
# else:
#     print("Odd")

#to find the greatest of three number entred by user

# a = int(input("Enter your first number: "))
# b = int(input("Enter your second number: "))
# c = int(input("Enter your third number: "))

# if(a >= b and a >= c):
#     print(f"First number is largest number which is: {a}")
# elif(b >= c):
#     print(f"Second number is largest number which is: {b}")
# else:
#     print(f"Third number is largest number which is: {c}")


#to check the number is multiple of 9 or not

# x = int(input("Enter your number: "))

# if(x % 9 == 0):
#     print("This number is multiple of 9")
# else:
#     print("your number is not multiple")


a = 8000
percentage = 8000 * 3/100
print(percentage)