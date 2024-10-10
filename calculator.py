# print(15+6)
# print(15-6)
# print(15*6)
# print(15/6)
# print(5**3)
# print(15%6)
# print(15//6)

# Create a Calculator capable of performing addition, subtraction, multiplication and division operations on two numbers.Your program should format the output in a readable manner!

# a = 50
# b = 4
# print("The Value of", a, "+", b, "is:", a + b)
# print("The Value of", a, "-", b, "is:", a - b)
# print("The Value of", a, "*", b, "is:", a * b)
# print("The Value of", a, "/", b, "is:", a / b)

print("**********Calculator**********")

num1 = int(input("Enter the first number = "))
num2 = int(input("Enter the second number = "))

# print("Choose the option which you want to apply")

# print("Press 1 for Addition")
# print("Press 2 for Subtraction")
# print("Press 3 for Multiplication")
# print("Press 4 for Division")
# print("Press 5 for Modulus")
# print("Press 6 for Exponential")
# print("Press 7 for Floor Division")

# type = int(input("Choose the option = "))

add = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2
mod = num1 % num2
exp = num1 ** num2
flo = num1 // num2

print("The Addition of", num1, "+", num2, "is = ", add)
print("The Subtraction of", num1, "-", num2, "is = ", sub)
print("The Multiplication of", num1, "*", num2, "is = ",mul)
print("The Division of", num1, "/", num2, "is = ",div)
print("The Modulus of", num1, "%", num2, "is = ",mod)
print("The Exponential of", num1, "**", num2, "is = ",exp)
print("The Floor Division of", num1, "//", num2, "is = ",flo)