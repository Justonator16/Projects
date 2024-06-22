#This projects calcualtes the sum,difference,product and division of fractions

#first step get numberator and denominator of a fraction 
def get_numerator(fraction):
    numerator = [ int(fraction[:i]) for i in range(len(fraction)) if fraction[i] == "/" ]
    return numerator[0]

def get_denominator(fraction):
    #The +1 starts the string slicing at the number after the / char
    denominator = [ int(fraction[i+1:]) for i in range(len(fraction)) if fraction[i] == "/"]
    return denominator[0]

def simplify_solution(fraction):
    numerator_solution = get_numerator(fraction)
    denominator_solution = get_denominator(fraction)

    #Find common factors of numerator and denominator
    common_factors = [ num1 for num1 in range(1,numerator_solution) if numerator_solution % num1 == 0 and denominator_solution % num1 == 0]

    #Next divide the numerator and denominator with the highest common factor
    if len(common_factors) != 0:
        simplified_numerator = numerator_solution / max(common_factors)
        simplified_denominator = denominator_solution / max(common_factors)

        final_solution = [str(int(simplified_numerator)),"/", str(int(simplified_denominator))]

    return "".join(final_solution)

def solution_of_two_fractions_based_on_operator(fraction1,fraction2,operator):
    f1_numerator = get_numerator(fraction1)
    f2_numerator = get_numerator(fraction2)

    f1_denominator = get_denominator(fraction1)
    f2_denominator = get_denominator(fraction2)

    if operator == "+":
        numerator_simplify = (f1_numerator * f2_denominator) + (f2_numerator * f1_denominator)
        denominator_simplify = f1_denominator * f2_denominator
    elif operator == "-":
        numerator_simplify = (f2_denominator * f1_numerator) - (f1_denominator * f2_numerator)
        denominator_simplify = f1_denominator * f2_denominator
    elif operator == "x":
        numerator_simplify = f1_numerator * f2_numerator
        denominator_simplify = f1_denominator * f2_denominator
    else:
        numerator_simplify = f1_numerator * f2_denominator
        denominator_simplify = f1_denominator * f2_numerator

    final_solution = [str(numerator_simplify),"/", str(denominator_simplify)]

    return "".join(final_solution)

fraction1 = input("Enter fraction here: ")
user_operation = input("Enter operation +,-,x,/ here: ")
fraction2 = input("Enter second fraction here: ")

operators = ["+","-","x","*","/"]
if user_operation in operators:
    print("Solution to its simplest form ",simplify_solution(solution_of_two_fractions_based_on_operator(fraction1,fraction2,user_operation)))
else:
    print("Invalid operator :( ")
