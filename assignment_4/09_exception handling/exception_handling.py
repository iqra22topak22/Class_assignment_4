# # the try block 
# # try:
# #     number :int = int(input("enter  a number :"))
# #     result = 10 / number
# #     print(result)
# # except:
#     # print("invalid input")

# # Specific error catch karna – jaise ZeroDivisionError, ValueError, etc. 
# try:
#     num : int = int(input("enter a nuber :"))
#     result = 10 / num 
#     print(" RESULT", result)
# except ZeroDivisionError:
#     print("can't divide by zero")

# # Generic except – jo har tarah ki error ko pakad leta hai.
# try:
#     number = int(input("Koi number daalo: "))
#     result = 10 / number
#     print("Result:", result)
# except:
#     print("Kuch to ghalat hua hai, check karo kya input diya tha.")


# #  Else Block

# try:
#     number = int(input("Koi number daalo: "))
#     result = 10 / number
# except ZeroDivisionError:
#     print("0 se divide nahi ho sakta!")
# except ValueError:
# #     print("Sirf number daalo, letters nahi!")
# # else:
# #     print("Sab theek tha, result hai:", result)


# try: 
#     num = int(input("enter a number :"))
#     result = 10 / num
# except ZeroDivisionError:
#     print("can't divide by zero")
# except ValueError:
#     print("sirf number lakho , latter nahi")

# else:
#     print("Sab theek tha, result hai:", result)


# finally block: 
try:
    num = int(input("enter a number: "))
    result= 10/ num
    print("Result" , result)
except ZeroDivisionError:
    print("can't divide by zero")
except ValueError:
    print("sirf number lakho , latter nahi")

finally:
    print("finally block")


# try:
#     file = open("data.txt", "r")
#     data = file.read()
#     print("File ka data:", data)
# except FileNotFoundError:
#     print("File nahi mili.")
# finally:
#     print("Ab file ko close kar rahe hain (ya kuch aur clean-up kar rahe hain).")


