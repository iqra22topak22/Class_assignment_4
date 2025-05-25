# # # Python mein function ek block of code hota hai jo kisi kaam ko perform karta hai.  

# # def print_fun():
# #     return "hello world"

# # print(print_fun())
# # # ----------------------------
# # def greetings():
# #    "This is docstring of greetings function"
# #    greet = 'Hello World!'
# #    return greet

# # message = greetings()
# # print(message)

# # # =====================================
# # # Python uses Pass by Object Reference.

# # # Agar object immutable ho (jaise int, str, tuple) → copy jaisa behave karta hai.

# # # Agar object mutable ho (jaise list, dict) → asli cheez modify ho jaati hai.

# # # def modify_value(x):
# # #     x = 10
# # #     print("Within function:", x)

# # # # Immutable object (integer)
# # # x = 5
# # # print("Original:", x)
# # # modify_value(x)
# # # print("After function:", x)

# # # --------------------------------------------
# # def cange_value(b):
# #     b= 1
# #     print("within fun", b)
# # b= 5
# # print("originaal", b)
# # cange_value(b)
# # print("after fun", b)
# # # ******************************************************
# # def value_change(a):
# #     a=5
# #     print("within function", a)

# # a =10
# # print("original", 0)
# # value_change(a)
# # print("after function,,", a)
# # # =====================================================

# # def modify_list(lst):
# #     lst.append(4)
# #     print("Within function: ", lst, " - ID:", id(lst))

# # # Mutable object (list)
# # lst = [1, 2, 3]
# # print("Original:", lst, " - ID:", id(lst))
# # modify_list(lst)
# # print("After function:", lst, " - ID:", id(lst))


# # # Function Arguments 
# # def add_num(a , b):
# #     sum = a + b
# #     return sum
# # print(add_num(10,10))

# # def greeting(name):
# #     print( "HELLO", name)
# #     return name

# # greeting("dua")

# # # ==============================================
# # # Keyword Arguments 

# # def printinfo( name, age ):
# #    "This prints a passed info into this function"
# #    print ("Name: ", name)
# #    print ("Age ", age)
# #    return name , age

# # # Now you can call printinfo function
# # printinfo( age=50, name="Arif" )
# # #printinfo(50, "Arif" )
# # # ----------------------------------------------------------------
# # def person_data(name,age,city):
# #     print(f"my name is {name} i am {age}year old and  i live in {city}")
# #     return name , age , city

# # person_data(name="iqra", age=20, city="karachi")
# # person_data(name="iqra", city="karachi", age=20)
# # # ----------------------------------------------------------

# # def add(x: int,y: int=0) -> float:
# #    return float(x + y)

# # print(float(add(10,20)))

# # print(add(y=50.0, x=2.0)) # type hints are not enforced in Python

# # print(add(x=5))

# # # ====================================================

# # def sum(a, b=0, c=10):
# #     print(a,b,c)
# #     return a +b + c

# # print(sum(10,20,10))
# # print(3)
# # print(sum(a=10, b=20,c=30))

# # *****************************************************

# #  Jab hum * ka use karte hain kisi iterable (jaise list, tuple) ke saath, to uska matlab hota hai "unpack karna", yaani uske andar ke elements ko alag-alag kar dena. 


# # def my_sum(*nums):
# #   print(type(nums),", ", nums)

# #   return sum(nums)

# # print("Sum     = ", my_sum(1,2,3,4,5,8,5),"\n")
# # print("Sum *[] = ", my_sum(*[1,2,3,4,5,8,5]), "\n") # *  unpacking list
# # print("Sum *() = ", my_sum(*(1,2,3,4,5,8,5))) # *  unpacking tuple
 
# # ===========================================================
# # **kwargs aik function mein use hota hai jab humein nahi pata hota ke kitne keyword arguments (named arguments) pass honge. Ye un sab ko ek dictionary ki form mein le leta hai.

# # def my_data(**kwarge):
# #     print(type(kwarge))
# #     for key,value in kwarge.items():
# #        print(f"{key} = {value}")

# # my_data(name="iqra", age=20, city="karachi")

# # ------------------------------------------------------------------

# # def my_function(**student):
# #   print("\nHis last name is " + student["lname"])

# #   for key, value in student.items():
# #     print(key, value)

# #   print(student)

# # my_function(fname = "Ali", lname = "Osman")

# # my_function(fname = "Ali", lname = "Osman", course = "Python - 101", day="Saturday", time="1400 - 1800")

# # my_dict = {"fname": "Arif", "lname": "Rozani", "course":"101 - 201", "day":"Saturday | Sunday", "role":"Student"}

# # #my_function(my_dict) # uncomment to see TypeError
# # my_function(**my_dict) # use ** to unpack the dictionary

# # # ----------------------------------------------------------

# # # Scope of Variables 

total = 0 # This is global variable.
# Function definition is here
def sum( arg1, arg2 ):
   # Add both the parameters and return them."
   total = arg1 + arg2; # Here total is local variable.
   print ("Inside the function local total : ", total)
   return total

# Now you can call sum function
sum( 10, 20 )
print ("Outside the function global total : ", total)
# # # ==============================================================
# # total = 1
# # def sum(num1 , num2):
# #   total = num1 + num2
# #   print("local total", total)
# #   return total

# # sum(20,20)

# # print(total)


# # Anonymous Functions (lambda functions)
# # Anonymous ka matlab hota hai "naam ke bagair". To anonymous functions wo functions hote hain jinka koi naam nahi hota. Inko hum def se define nahi karte, balki lambda keyword se banate hain.

# add = lambda x,y : x + y
# print(add(10,20))


# name = lambda first_name, f_name: f"my name is {first_name} {f_name}"
# print(name("iqra".upper()," mushtaq"))
# # ---------------------------------------------------

is_palindrome = lambda s: s == s[::-1]

print(is_palindrome("madam"))  # Output: True
print(is_palindrome("hello"))  # Output: False


def add_two(x, y):
  return x + y

my_lambda = lambda x, y:  x + y

print(my_lambda(1,2))

# ---------------------------------------------------------------------

#  Summary in Simple Steps:

# Step	Kya Ho Raha Hai
# def simple_generator()	     Generator function define kiya
# gen = simple_generator()    	Generator object bana
# print(gen)	                  Generator ka type dikhaya
# for value in gen:	            Har yield wali value mil rahi hai
# print(value)              	 Value aur uska type print ho raha hai

def simple_generator():
    yield 1
    yield 2
    yield 3

# Create a generator object
gen = simple_generator()

print(gen, " : ", type(gen))

# Iterate over the generator
for value in gen:
    print(value, " : ", type(value))










