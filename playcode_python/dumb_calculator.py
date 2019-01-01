'''
Make a simple numeric calculator. It should prompt the user for three numbers. Then add the numbers together and divide by 2. Display the result. Your program must support numbers with decimals and not just integers.
'''

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

total = (num1 + num2 + num3) / 2

print(total)
#print("Output: ",total)