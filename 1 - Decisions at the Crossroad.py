#You are provided with a Python script that uses conditional statements to tell if a number is positive, negative, or zero, but it has some errors. Identify and fix them.

number = int(input("Enter a number: ")) #added type cast to allow for conditions in if/elif/else to be evaluated

if number > 0:
    print("The number is positive.")
elif number == 0: #missing 2nd = to make it an evaluation instead of an assignment
    print("The number is zero.")
else: #else does not evaluate conditions like elif
    print("The number is negative.")
