# URI Beginner Problems

# SUBJECT: SEQUENTIAL

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

| Input Sample   | Output Samples     |
| -------------- | ------------------ |
| 3.0 4.0 5.2    | TRIANGULO: 7.800   |
|                | CIRCULO: 84.949    |
|                | TRAPEZIO: 18.200   |
|                | QUADRADO: 16.000   |
|                | RETANGULO: 12.000  |
| 12.7 10.4 15.2 | TRIANGULO: 96.520  |
|                | CIRCULO: 725.833   |
|                | TRAPEZIO: 175.560  |
|                | QUADRADO: 108.160  |
|                | RETANGULO: 132.080 |


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


## 1016 - Distance

Two cars (X and Y) leave in the same direction. The car X leaves with a constant speed of 60 km/h and the car Y leaves with a constant speed of 90 km / h.

In one hour (60 minutes) the car Y can get a distance of 30 kilometers from the X car, in other words, it can get away one kilometer for each 2 minutes.

Read the distance (in km) and calculate how long it takes (in minutes) for the car Y to take this distance in relation to the other car.

**Input**

The input file contains 1 integer value.

**Output**

Print the necessary time followed by the message "minutos" that means minutes in Portuguese.

| Input Sample | Output Samples |
| ------------ | -------------- |
| 30           | 60 minutos     |
| 110          | 220 minutos    |
| 7            | 14 minutos     |


## 1017 - Fuel Spent

Little John wants to calculate and show the amount of spent fuel liters on a trip, using a car that does 12 Km/L. For this, he would like you to help him through a simple program. To perform the calculation, you have to read spent time (in hours) and the same average speed (km/h). In this way, you can get distance and then, calculate how many liters would be needed. Show the value with three decimal places after the point.

**Input**

The input file contains two integers. The first one is the spent time in the trip (in hours). The second one is the average speed during the trip (in Km/h).

**Output**

Print how many liters would be needed to do this trip, with three digits after the decimal point.

| Input Sample | Input Sample | Output Samples |
| ------------ | ------------ | -------------- |
| 10           | 85           | 70.833         |
| 2            | 92           | 15.333         |
| 22           | 67           | 122.833        |


## 1018 - Banknotes

In this problem you have to read an integer value and calculate the smallest possible number of banknotes in which the value may be decomposed. The possible banknotes are 100, 50, 20, 10, 5, 2 e 1. Print the read value and the list of banknotes.

**Input**

The input file contains an integer value N (0 < N < 1000000).

**Output**

Print the read number and the minimum quantity of each necessary banknotes in Portuguese language, as the given example. Do not forget to print the end of line after each line, otherwise you will receive “Presentation Error”.

| Input Sample | Output Samples           |
| ------------ | ------------------------ |
| 576          | 576                      |
|              | 5 nota(s) de R$ 100,00   |
|              | 1 nota(s) de R$ 50,00    |
|              | 1 nota(s) de R$ 20,00    |
|              | 0 nota(s) de R$ 10,00    |
|              | 1 nota(s) de R$ 5,00     |
|              | 0 nota(s) de R$ 2,00     |
|              | 1 nota(s) de R$ 1,00     |
| 11257        | 11257                    |
|              | 112 nota(s) de R$ 100,00 |
|              | 1 nota(s) de R$ 50,00    |
|              | 0 nota(s) de R$ 20,00    |
|              | 0 nota(s) de R$ 10,00    |
|              | 1 nota(s) de R$ 5,00     |
|              | 1 nota(s) de R$ 2,00     |
|              | 0 nota(s) de R$ 1,00     |
| 503          | 503                      |
|              | 5 nota(s) de R$ 100,00   |
|              | 0 nota(s) de R$ 50,00    |
|              | 0 nota(s) de R$ 20,00    |
|              | 0 nota(s) de R$ 10,00    |
|              | 0 nota(s) de R$ 5,00     |
|              | 1 nota(s) de R$ 2,00     |
|              | 1 nota(s) de R$ 1,00     |


## 1019 - Time Conversion

Read an integer value, which is the duration in seconds of a certain event in a factory, and inform it expressed in hours:minutes:seconds.

**Input**

The input file contains an integer N.

**Output**

Print the read time in the input file (seconds) converted in hours:minutes:seconds like the following example.

| Input Sample | Output Samples |
| ------------ | -------------- |
| 556          | 0:9:16         |
| 1            | 0:0:1          |
| 140153       | 38:55:53       |


## 1020 - Age in Days

Read an integer value corresponding to a person's age (in days) and print it in years, months and days, followed by its respective message “ano(s)”, “mes(es)”, “dia(s)”.

Note: only to facilitate the calculation, consider the whole year with 365 days and 30 days every month. In the cases of test there will never be a situation that allows 12 months and some days, like 360, 363 or 364. This is just an exercise for the purpose of testing simple mathematical reasoning.

**Input**

The input file contains 1 integer value.

**Output**

Print the output, like the following example.

| Input Sample | Output Samples |
| ------------ | -------------- |
| 400          | 1 ano(s)       |
|              | 1 mes(es)      |
|              | 5 dia(s)       |
| 800          | 2 ano(s)       |
|              | 2 mes(es)      |
|              | 10 dia(s)      |
| 30           | 0 ano(s)       |
|              | 1 mes(es)      |
|              | 0 dia(s)       |


## 1021 - Banknotes and Coins

Read a value of floating point with two decimal places. This represents a monetary value. After this, calculate the smallest possible number of notes and coins on which the value can be decomposed. The considered notes are of 100, 50, 20, 10, 5, 2. The possible coins are of 1, 0.50, 0.25, 0.10, 0.05 and 0.01. Print the message “NOTAS:” followed by the list of notes and the message “MOEDAS:” followed by the list of coins.

**Input**

The input file contains a value of floating point N (0 ≤ N ≤ 1000000.00).


**Output**

Print the minimum quantity of banknotes and coins necessary to change the initial value, as the given example.


| Input Sample | Output Samples         |
| ------------ | ---------------------- |
| 576.73       | NOTAS:                 |
|              | 5 nota(s) de R$ 100.00 |
|              | 1 nota(s) de R$ 50.00  |
|              | 1 nota(s) de R$ 20.00  |
|              | 0 nota(s) de R$ 10.00  |
|              | 1 nota(s) de R$ 5.00   |
|              | 0 nota(s) de R$ 2.00   |
|              | MOEDAS:                |
|              | 1 moeda(s) de R$ 1.00  |
|              | 1 moeda(s) de R$ 0.50  |
|              | 0 moeda(s) de R$ 0.25  |
|              | 2 moeda(s) de R$ 0.10  |
|              | 0 moeda(s) de R$ 0.05  |
|              | 3 moeda(s) de R$ 0.01  |
| 4.00         | NOTAS:                 |
|              | 0 nota(s) de R$ 100.00 |
|              | 0 nota(s) de R$ 50.00  |
|              | 0 nota(s) de R$ 20.00  |
|              | 0 nota(s) de R$ 10.00  |
|              | 0 nota(s) de R$ 5.00   |
|              | 2 nota(s) de R$ 2.00   |
|              | MOEDAS:                |
|              | 0 moeda(s) de R$ 1.00  |
|              | 0 moeda(s) de R$ 0.50  |
|              | 0 moeda(s) de R$ 0.25  |
|              | 0 moeda(s) de R$ 0.10  |
|              | 0 moeda(s) de R$ 0.05  |
|              | 0 moeda(s) de R$ 0.01  |
| 91.01        | NOTAS:                 |
|              | 0 nota(s) de R$ 100.00 |
|              | 1 nota(s) de R$ 50.00  |
|              | 2 nota(s) de R$ 20.00  |
|              | 0 nota(s) de R$ 10.00  |
|              | 0 nota(s) de R$ 5.00   |
|              | 2 nota(s) de R$ 2.00   |
|              | MOEDAS:                |
|              | 1 moeda(s) de R$ 1.00  |
|              | 0 moeda(s) de R$ 0.50  |
|              | 0 moeda(s) de R$ 0.25  |
|              | 0 moeda(s) de R$ 0.10  |
|              | 0 moeda(s) de R$ 0.05  |
|              | 1 moeda(s) de R$ 0.01  |


# SUBJECT: SELECTION

## 1035 - Selection Test 1

Read 4 integer values A, B, C and D. Then if B is greater than C and D is greater than A and if the sum of C and D is greater than the sum of A and B and if C and D were positives values and if A is even, write the message “Valores aceitos” (Accepted values). Otherwise, write the message “Valores nao aceitos” (Values not accepted).

**Input**

Four integer numbers A, B, C and D.

**Output**

Show the corresponding message after the validation of the values​​.

| Input Sample | Output Samples      |
| ------------ | ------------------- |
| 5 6 7 8      | Valores nao aceitos |
| 2 3 2 6      | Valores aceitos     |


## 1036 - Bhaskara's Formula

Read 3 floating-point numbers. After, print the roots of bhaskara’s formula. If it's impossible to calculate the roots because a division by zero or a square root of a negative number, presents the message “Impossivel calcular”.

**Input**

Read 3 floating-point numbers A, B and C.

**Output**

Print the result with 5 digits after the decimal point or the message if it is impossible to calculate.

| Input Sample   | Output Samples      |
| -------------- | ------------------- |
| 10.0 20.1 5.1  | R1 = -0.29788       |
|                | R2 = -1.71212       |
| 0.0 20.0 5.0   | Impossivel calcular |
| 10.3 203.0 5.0 | R1 = -0.02466       |
|                | R2 = -19.68408      |
| 10.0 3.0 5.0   | Impossivel calcular |


## 1037 - Interval

You must make a program that read a float-point number and print a message saying in which of following intervals the number belongs: [0,25] (25,50], (50,75], (75,100]. If the read number is less than zero or greather than 100, the program must print the message “Fora de intervalo” that means "Out of Interval".

The symbol '(' represents greather than. For example:
[0,25] indicates numbers between 0 and 25.0000, including both.
(25,50] indicates numbers greather than 25 (25.00001) up to 50.0000000.

**Input**

The input file contains a floating-point number.

**Output**

The output must be a message like following example.

| Input Sample | Output Samples     |
| ------------ | ------------------ |
| 25.01        | Intervalo (25,50]  |
| 25.00        | Intervalo [0,25]   |
| 100.00       | Intervalo (75,100] |
| -25.02       | Fora de intervalo  |


## 1038 - Snack

Using the following table, write a program that reads a code and the amount of an item. After, print the value to pay. This is a very simple program with the only intention of practice of selection commands.

| CODE | SPECIFICATION   | PRICE  |
| 1    | Cachorro Quente | R$4.00 |
| 2    | X-Salada        | R$4.50 |
| 3    | X-Bacon         | R$5.00 |
| 4    | Torrada simples | R$2.00 |
| 5    | Refrigerante    | R$1.50 |

**Input**

The input file contains two integer numbers X and Y. X is the product code and Y is the quantity of this item according to the above table.

**Output**

The output must be a message "Total: R$ " followed by the total value to be paid, with 2 digits after the decimal point.

| Input Sample | Output Samples  |
| ------------ | --------------- |
| 3 2          | Total: R$ 10.00 |
| 4 3          | Total: R$ 6.00  |
| 2 3          | Total: R$ 13.50 |







***

## 10 - 



**Input**



**Output**



| Input Sample | Output Samples           |
| ------------ | ------------------------ |
|              |  