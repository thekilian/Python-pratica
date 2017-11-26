# URI Beginner Problems

## 1001 - Extremely basic

Read 2 integer values and store them in variables, named A and B and make the sum of these two variables, assigning its result to the variable X. Print X as shown below. Don't present any message beyond what is being specified and don't forget to print the end of line after the result, otherwise you will receive “Presentation Error”.

**Input**

The input file contain 2 integer values.

**Output**

Print the variable X according to the following example, with a blank space before and after the equal signal. 'X' is uppercase and you have to print a blank space before and after the '=' signal.

| Input Sample | Input Sample | Output Samples |
| ------------ | ------------ | -------------- |
| 10           | 9            | X = 19         |
|-10           | 4            | X = -6         |
| 15           | -7           | X = 8          |

## 1002 - Area of a Circle

The formula to calculate the area of a circumference is defined as A = π . R2. Considering to this problem that π = 3.14159:

Calculate the area using the formula given in the problem description.

**Input**

The input contains a value of floating point (double precision), that is the variable R.

**Output**

Present the message "A=" followed by the value of the variable, as in the example bellow, with four places after the decimal point. Use all double precision variables. Like all the problems, don't forget to print the end of line after the result, otherwise you will receive "Presentation Error".              

| Input Sample | Output Samples |
| ------------ | -------------- |
| 12.0         | A=12.5664      |
| 100.64       | A=31819.3103   |
| 150.00       | A=70685.7750   |


## 1003 - Simple Sum

Read two integer values, in this case, the variables A and B. After this, calculate the sum between them and assign it to the variable SOMA. Write the value of this variable.

**Input**

The input file contains 2 integer numbers.

**Output**

Print the variable SOMA with all the capital letters, with a blank space before and after the equal signal followed by the corresponding value to the sum of A and B. Like all the problems, don't forget to print the end of line, otherwise you will receive "Presentation Error"

| Input Sample | Input Sample | Output Samples |
| ------------ | ------------ | -------------- |
| 30           | 10           | SOMA = 40      |
|-30           | 10           | SOMA = -20     |
| 0            | 0            | SOMA = 0       |


## 1004 - Simple Product

Read two integer values. After this, calculate the product between them and store the result in a variable named PROD. Print the result like the example below. Do not forget to print the end of line after the result, otherwise you will receive “Presentation Error”.

**Input**

The input file contains 2 integer numbers.

**Output**

Print PROD according to the following example, with a blank space before and after the equal signal.

| Input Sample | Input Sample | Output Samples |
| ------------ | ------------ | -------------- |
| 3            | 9            | PROD = 27      |
|-30           | 10           | PROD = -300    |
| 0            | 9            | PROD = 0       |


## 1005 - Average 1

Read two floating points' values of double precision A and B, corresponding to two student's grades. After this, calculate the student's average, considering that grade A has weight 3.5 and B has weight 7.5. Each grade can be from zero to ten, always with one digit after the decimal point. Don’t forget to print the end of line after the result, otherwise you will receive “Presentation Error”. Don’t forget the space before and after the equal sign.

**Input**

The input file contains 2 floating points' values with one digit after the decimal point.

**Output**

Print MEDIA(average in Portuguese) according to the following example, with 5 digits after the decimal point and with a blank space before and after the equal signal.

| Input Sample | Input Sample | Output Samples   |
| ------------ | ------------ | ---------------- |
| 5.0          | 7.1          | MEDIA = 6.43182  |
| 0.0          | 7.1          | MEDIA = 4.84091  |
| 10.0         | 10.0         | MEDIA = 10.00000 |


## 1006 - Average 2

Read three values (variables A, B and C), which are the three student's grades. Then, calculate the average, considering that grade A has weight 2, grade B has weight 3 and the grade C has weight 5. Consider that each grade can go from 0 to 10.0, always with one decimal place.

**Input**

The input file contains 3 values of floating points with one digit after the decimal point.

**Output**

Print MEDIA(average in Portuguese) according to the following example, with a blank space before and after the equal signal.

| Input Sample | Input Sample | Input Sample | Output Samples |
| ------------ | ------------ | ------------ | -------------- |
| 5.0          |  6.0         |  7.0         | MEDIA = 6.3    |
| 5.0          | 10.0         | 10.0         | MEDIA = 9.0    |
| 10.0         | 10.0         |  5.0         | MEDIA = 7.5    |


## 1007 - Difference

Read four integer values named A, B, C and D. Calculate and print the difference of product A and B by the product of C and D (A * B - C * D).

**Input**

The input file contains 4 integer values.

**Output**

Print DIFERENCA (DIFFERENCE in Portuguese) with all the capital letters, according to the following example, with a blank space before and after the equal signal.

| Input Sample | Input Sample | Input Sample | Input Sample | Output Samples  |
| ------------ | ------------ | ------------ | ------------ | --------------- |
| 5            | 6            |  7           | 8            | DIFERENCA = -26 |
| 0            | 0            |  7           | 8            | DIFERENCA = -56 |
| 5            | 6            | -7           | 8            | DIFERENCA = 86  |


## 1008 - Salary

Write a program that reads an employee's number, his/her worked hours number in a month and the amount he received per hour. Print the employee's number and salary that he/she will receive at end of the month, with two decimal places.

**Input**

The input file contains 2 integer numbers and 1 value of floating point, representing the number, worked hours amount and the amount the employee receives per worked hour.

**Output**

Print the number and the employee's salary, according to the given example, with a blank space before and after the equal signal.

| Input 1 | Input 2 | Input 3 | Output 1    | Output 2            |
| ------- | ------- | ------- | ----------- | ------------------- |
| 25      | 100     |  5.50   | NUMBER = 25 | SALARY = U$ 550.00  |
|  1      | 200     | 20.50   | NUMBER = 1  | SALARY = U$ 4100.00 |
|  6      | 145     | 15.55   | NUMBER = 6  | SALARY = U$ 2254.75 |


## 1009 - Salary with Bonus

Make a program that reads a seller's name, his/her fixed salary and the sale's total made by himself/herself in the month (in money). Considering that this seller receives 15% over all products sold, write the final salary (total) of this seller at the end of the month , with two decimal places.

**Input**

The input file contains a text (employee's first name), and two double precision values, that are the seller's salary and the total value sold by him/her.

**Output**  

Print the seller's total salary, according to the given example.

| Input 1 | Input 2 | Input 3  | Output             |
| ------- | ------- | -------- | ------------------ |
| JOAO    | 500.00  | 1230.30  | TOTAL = R$ 684.54  |
| PEDRO   | 700.00  | 0.00     | TOTAL = R$ 700.00  |
| PAULO   | 1700.00 | 1230.50  | TOTAL = R$ 1884.58 |


## 1010 - Simple Calculate

In this problem, the task is to read a code of a product 1, the number of units of product 1, the price for one unit of product 1, the code of a product 2, the number of units of product 2 and the price for one unit of product 2. After this, calculate and show the amount to be paid.

**Input**

The input file contains two lines of data. In each line there will be 3 values: two integers and a floating value with 2 digits after the decimal point.

**Output**

The output file must be a message like the following example where "Valor a pagar" means Value to Pay. Remember the space after ":" and after "R$" symbol. The value must be presented with 2 digits after the point.

| Input 1    | Input 2    | Output                  |
| ---------- | ---------- | ----------------------- |
| 12 1 5.30  | 16 2 5.10  | VALOR A PAGAR: R$ 15.50 |
| 13 2 15.30 | 161 4 5.20 | VALOR A PAGAR: R$ 51.40 |
| 1 1 15.10  | 2 1 15.10  | VALOR A PAGAR: R$ 30.20 |


## 1011 - Sphere

Make a program that calculates and shows the volume of a sphere being provided the value of its radius (R) . The formula to calculate the volume is: (4/3) * pi * R3. Consider (assign) for pi the value 3.14159.

Tip: Use (4/3.0) or (4.0/3) in your formula, because some languages (including C++) assume that the division's result between two integers is another integer. :)

**Input**

The input contains a value of floating point (double precision).

**Output**

The output must be a message "VOLUME" like the following example with a space before and after the equal signal. The value must be presented with 3 digits after the decimal point.

| Input Sample | Output Samples           |
| ------------ | ------------------------ |
| 3            | VOLUME = 113.097         |
| 15           | VOLUME = 14137.155       |
| 1523         | VOLUME = 14797486501.627 |


## 1012 - Area

Make a program that reads three floating point values: A, B and C. Then, calculate and show:
a) the area of the rectangled triangle that has base A and height C.
b) the area of the radius's circle C. (pi = 3.14159)
c) the area of the trapezium which has A and B by base, and C by height.
d) the area of ​​the square that has side B.
e) the area of the rectangle that has sides A and B.

**Input**

The input file contains three double values with one digit after the decimal point.

**Output**

The output file must contain 5 lines of data. Each line corresponds to one of the areas described above, always with a corresponding message (in Portuguese) and one space between the two points and the value. The value calculated must be presented with 3 digits after the decimal point.
Input Samples 	Output Samples

| Input Sample   | Output Samples           |
| -------------- | ------------------------ |
| 3.0 4.0 5.2    | TRIANGULO: 7.800         |
                 | CIRCULO: 84.949          |
                 | TRAPEZIO: 18.200         |
                 | QUADRADO: 16.000         |
                 | RETANGULO: 12.000        |
                 
| 12.7 10.4 15.2 | TRIANGULO: 96.520        |
                 | CIRCULO: 725.833         |
                 | TRAPEZIO: 175.560        |
                 | QUADRADO: 108.160        |
                 | RETANGULO: 132.080       |


## 1013 - The Greatest

Make a program that reads 3 integer values and present the greatest one followed by the message "eh o maior". Use the following formula:

MaiorAB = (a+b+abs(a-b))/2

**Input**

The input file contains 3 integer values.

**Output**

Print the greatest of these three values followed by a space and the message “eh o maior”.

| Input Sample | Output Samples |
| ------------ | -------------- |
| 7 14 106     | 106 eh o maior |
| 217 14 6     | 217 eh o maior |


## 1014 - Consumption

Calculate a car's average consumption being provided the total distance traveled (in Km) and the spent fuel total (in liters).

**Input**

The input file contains two values: one integer value X representing the total distance (in Km) and the second one is a floating point number Y  representing the spent fuel total, with a digit after the decimal point.

**Output**

Present a value that represents the average consumption of a car with 3 digits after the decimal point, followed by the message "km/l".

| Input Sample | Input Sample | Output Samples |
| ------------ | ------------ | -------------- |
| 500          | 35.0         | 14.286 km/l    |
| 2254         | 124.4        | 18.119 km/l    |
| 4554         | 464.6        | 9.802 km/l     |


## 1015 - Distance between two points

Read the four values corresponding to the x and y axes of two points in the plane, p1 (x1, y1) and p2 (x2, y2) and calculate the distance between them, showing four decimal places after the comma, according to the formula:

Distance = RAIZ (x2 - x1)² + (y2 - y1)²

**Input**

The input file contains two lines of data. The first one contains two double values: x1 y1 and the second one also contains two double values with one digit after the decimal point: x2 y2.

**Output**

Calculate and print the distance value using the provided formula, with 4 digits after the decimal point.

| Input Sample | Input Sample | Output Samples |
| ------------ | ------------ | -------------- |
| 1.0 7.0      | 5.0 9.0      | 4.4721         |
| -2.5 0.4     | 12.1 7.3     | 16.1484        |
| 2.5 -0.4     | -12.2 7.0    | 16.4575        |

