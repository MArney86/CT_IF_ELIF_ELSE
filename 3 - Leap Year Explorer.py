#Task 1: Leap Year Checker

year = int(input("What year do you want to test?: ")) #input year to test whether it is a leap year or not

if year % 4 == 0 and year % 100 == 0 and year % 400 == 0: #test if year is divisible by 4, 100 and 400 to check for ultimate leap year conditions
    print(str(year) + " is a leap year")
elif year % 4 == 0 and year % 100 != 0: #check if year is divisible by 4 and not 100 since we know it's not divisible by 400 if we got this far
    print(str(year) + " is a leap year")
else: 
    print(str(year) + " is not a leap year") #message to print if year is not divisible by 4, or is divisble by 4 but also 100 and not 400 (no need to test for 400 since we wouldn't get here if it was)  