# def divide_value(a:int , b:int) -> int:
#     try:
#         result = a/b
#         print(f"print successfully " ,{result})
#         return result
    
#     except ZeroDivisionError:
#         print("can not divide by zero")
#         return 0
    
# print(divide_value(10,0))
# print(divide_value(10,2))
# --------------------------------------------------------

# # else block 

# def divide_value(a: int, b: int) -> float:
#     try:
#         result = a / b
#     except ZeroDivisionError:
#         print("❌ Error: Cannot divide by zero.")
#         return 0
#     else:
#         print("✅ Else block: Division successful.")
#         print(f"📊 Result is: {result}")
#         return result
    
# print(divide_value(10,2))
# print(divide_value(10,0))

# -----------------------------------------------------
# try:
#     number = int("10")
# except ValueError:
#     print("Yeh ghalat input tha.")
# else:
#     print("Sab sahi tha! Tumhara number hai:", number)

# --------------------------------------------------------

# def fun(a,b):
#     try: 
#         result = a / b
#     except ZeroDivisionError:
#         print("cant noty adivive by 0")
#         return 0 

#     else:
#         print("else block")   
#         return result 

# print(fun(10,2))

# # --------------------------------------------
# try:
#     file = open("non_existing_file.txt")
# except FileNotFoundError:
#     print("File nahi mili.")
# finally:
#     print("File system se nikal gaya, chahe file mili ya nahi.")


# Chahe error aaye ya na aaye, finally block hamesha run hota hai.
# try:
#    name :str = str(input("enter your name :"))

#    print(name)
# except ValueError:
#     print("invaild value")
# finally:
#     print("finally block")

# try:
#     number = int("10")
# except ValueError:
#     print("Yeh ghalat input tha.")
# else:
#     print("Sab sahi tha! Tumhara number hai:", number)

    
    
# def fun(a, b):
#     try:
#         result = a / b
#     except ZeroDivisionError:
#         print("❌ Error: Can't divide by 0")
#         return 0
#     else:
#         print("✅ Else block: Division successful")
#         return result
#     finally:
#         print("🧹 Finally block: Ye hamesha chalta hai.")

# # Test calls
# print("Result:", fun(10, 2))
# print("----")
# print("Result:", fun(5, 0))

def fun(a,b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("not divide ny zero")
        return 0
    else:
        print("good work")
        return result
    finally:
        print("chlty rhooo")

# print(fun(2,0))
print(fun(10,10))