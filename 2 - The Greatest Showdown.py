#Task 1: Identify the Greatest

number_1 = int(input("Enter first number: ")) #input for first number
number_2 = int(input("Enter second number: ")) #input for second number
number_3 = int(input("Enter last number: ")) #input for third number

if number_1 >= number_2 and number_1 >= number_3: #check if first number is largest
    print("The largest number is " + str(number_1))
elif number_2 >= number_1 and number_2 >= number_3: #check if second is largest if first isn't
    print("The largest number is " + str(number_2))
elif number_3 >= number_1 and number_3 >= number_2: #check if third is largest if second and first aren't
    print("The largest number is " + str(number_3))
else:
    print("Something went wrong") #error statement if logic fails

#Task 2: Identify the Smallest

if number_1 <= number_2 and number_1 <= number_3: #check if first number is smallest
    print("The smallest number is " + str(number_1))
elif number_2 <= number_1 and number_2 <= number_3: #check second if first is not smallest
    print("The smallest number is " + str(number_2))
elif number_3 <= number_1 and number_3 <= number_2: #check third if second and first are not smallest
    print("The smallest number is " + str(number_3))
else:
    print("Something went wrong") #error statement if logic fails
#Task 3: Equality Check

if number_1 == number_2 and number_1 == number_3: #check if all numbers are equal first
    print("All numbers are equal to each other")
elif number_1 == number_2 and number1 !=3: # if not all equal see if first and second are
    print("There are two numbers equal to each other, the first and second")
elif number_1 != number_2 and number_1 == number_3: #if first and second aren't equal check first and third
    print("There are two numbers equal to each other, the first and third")
elif number_2 == number_3 and number_2 != number_1: #if first and third aren't equal check second and third
    print("There are two numbers equal to each other, the second and third")
else:
    print("There are no numbers equal to each other") #message if no two or all three numbers are equal
