'''
Make a simple numeric calculator. It should prompt the user for three numbers. Then add the numbers together and divide by 2. Display the result. Your program must support numbers with decimals and not just integers.

Enter first number:1.1
Enter second number:2.2
Enter third number:5.5
Output:
(1.1+2.2+5.5)/2 is:4.4


Enter first number:2.2
Enter second number:3.3
Enter third number:1.1
Output:
(2.2+3.3+1.1)/2 is:3.3

***

num1 = input("Enter first number:")
num2 = input("Enter second number:")
num3 = input("Enter third number:")
#{Write down your logic here

#}
'''

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

total = num1 + num2 + num3 / 2

print("Output:" + total)


'''
Enter first number:1
Enter second number:1
Enter third number:1
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-23-7e1c17ebd5ee> in <module>()
      3 num3 = input("Enter third number:")
      4 
----> 5 total = num1 + num2 + num3 / 2
      6 
      7 print("Output:")

TypeError: unsupported operand type(s) for /: 'str' and 'int'
'''