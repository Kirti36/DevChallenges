# x = 3
# y = 4
#     print(x+y)
#     print(x-y)
#     print(x/y)
#     print(x//y)
#     print(x%y)
#     print(x*y)
#     x+=3
#     print("sum",x)
#     print(x>2 and x<1)
#     print(x>2 or x<1)


    # a= input("enter number")
    # for i in a:
    #     if(a%2==0):
    #         print("Even")
    #     else:
    #         print("odd")

# string = "{} {} {}".format('Python','Programming','language')
# print(string)


# statement = "Hey World "
# print(statement.upper())
# print(statement.lstrip('Hey'))
# print(statement.rstrip())

# name = "Kirti"
# course = "AI & DS"
# print(f"hello I'm {name} and pursuing {course}")

# string = "Moi Name is Kirti Parmar"
# string = input("ENter kuch b: ")
# print(string.split('a'))
# print(string)
# print(string[2:-1])
# print(string[:5])
# print(string[:])
# print(string[0:])
# print(string[:-1])

# lst=["kirti",2,23,24 , "Parmar", "ice cream"]
# print(lst)
# print(len(lst))
# print(type(lst))
# print(lst[3])
# lst.append("Mnnu")
# print(lst)
# lst.extend("Hello")
# lst.extend(["Hllo"])
# print(lst)
# lst.insert(3,"yuvi")
# print(lst)
# lst.pop(2)
# print(lst)
# lst1=["a","l","m","k","g"]
# lst1.sort()
# print(lst1)

# friuts_list = []
# friuts_list = ["apple","banana","orange","grape","mango"]
# print(friuts_list[0])
# print(friuts_list[-1])
# print(friuts_list[1])
# print(friuts_list[2])
# print(len(friuts_list))
# friuts_list[2]="pear"
# print(friuts_list)

# for i in range(0, len(friuts_list)):
#     if("apple" in friuts_list[i]):
#         print("Yes")
#     else:
#         print("No")

# friuts_list.remove("banana")
# friuts_list.remove("apple")
# print(friuts_list)

# # friuts_list = ["apple","banana","orange","grape","mango"]
# lst2 = ["watermelon","kiwi"]
# b = friuts_list+lst2
# print(b)
# friuts_list.sort()
# print(friuts_list)

# print(b.count("kiwi"))

# tup = ('water','happy','lol')
# tupp = ('kim')
# a = tup + tupp
# print(a)

# cars={1:"chevrolet", 2:"Toyota", 3:"Jaguar"}
# print(sorted(cars))
# print(dir(list))
# print(cars)
# print(type(cars))
# print(cars.keys())
# print(cars.values())
# print(cars.items())
# cars.update({3:"ferari"})
# print(cars)
# cars[2]= "Alto"
# print(cars)

# set1 = {2,3,45,6,6,4}
# print(set1)
# set2 = {4,55,646,46,5,4}
# print(set1|set2) 
# print(set1.union(set2))
# print(set1.intersection(set2)) 
# print(len(set1))

# def mul_nums(a,b,c):
#      mul = a* b*c
#      return mul
# print(mul_nums(2,4,6))

# en = int(input("Enter the number: "))
# if(en>0):
#     print("positive")
# elif(en<0):
#     print("negative")
# else:
#     print("the value is 0")

# counter = 0
# while counter<3:
#     counter+=1
# print("Yo")
   

# while counter < 3:
#     print("Yo")
#     counter+=1

# a = "hello world"
# for i in a:
#     print(i)

# a = (2,3,4,5,6)
# for i in a:
#     print(i)

# for i in range(0,11):
#     print(i)

# for i in range(0,11):
#     if(i%2!=0):
#         print(i)

# lst = ['a','b','c','d','e','f','g','h']
# for i in lst:
#     print(i)

# for i in range(0,101):
#     print(i)

# for i in range(0,11):
    
#     if(i>=5):
#         print(i)
#         continue
# print("\n")
# for i in range(0,11):
    
#     if(i>=5):
#         print(i)
#         break



# def bills(it, pr):
#     if(len(it)!=len(pr)):
#         return "404 ERROR"

#     bill = 0
#     for rs in pr:
#         bill = bill + rs
#     return bill

# itlist=["vanilla","Strawberry","chocolate"]
# prlist=[20,56,23,13]
# amount = bills(itlist, prlist)
# print("Amount is: ",amount)


# def discount(it, pr):
#     if(len(it)!=len(pr)):
#         return "404 ERROR"

#     bill = 0
#     for rs in pr:
#         if(rs>=30):
#             ("eligible for dicount")
#         for i in pr:
#             print(i)
#         bill = bill + (rs/10*100)
#     return bill
#     if(pr>=30):
#         ("eligible for dicount")
#         for i in pr:
#             print(i)

# itlist=["vanilla","Strawberry","chocolate"]
# prlist=[20,56,23]
# amount = discount(itlist, prlist)
# print("Amount is: ",amount)

# x = lambda x: x-19
# print(x(56))

# try:
#     num = int(input("Number: "))
#     den = int(input("Denominator: "))
#     res = num/den
#     print(res)
# except ZeroDivisionError:
#     print("ERROR: Cannot divide by zero")


# try:
#     num = int(input("Number: "))
# except ValueError:
#     print("Please enter a valid number")
# else:
#     cube = num*num*num
#     print("Cube of",num,"is",cube)
