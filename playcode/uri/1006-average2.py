'''
Read three values (variables A, B and C), which are the three student's grades. Then, calculate the average, considering that grade A has weight 2, grade B has weight 3 and the grade C has weight 5. Consider that each grade can go from 0 to 10.0, always with one decimal place.

Input

The input file contains 3 values of floating points with one digit after the decimal point.

Output

Print MEDIA(average in Portuguese) according to the following example, with a blank space before and after the equal signal.

Input Samples	Output Samples
5.0
6.0
7.0
                MEDIA = 6.3
5.0
10.0
10.0
                MEDIA = 9.0
10.0
10.0
5.0
                MEDIA = 7.5
'''
a = float(input()) # one digit after the decimal point?
b = float(input())
c = float(input())

# considering that grade A has weight 2, grade B has weight 3

media = (a + b + c) / 3

print("MEDIA = %1.1f" %(media))
# erro