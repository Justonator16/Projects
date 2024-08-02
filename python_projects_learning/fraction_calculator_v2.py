#This project has OOP and better readability compared to the first version
#Interesting idea include a way for users to calculate as many numbers as possible

class FractionCalculator:
    def __init__(self, fraction1 : str, fraction2 : str):
        self.fraction1 = fraction1
        self.fraction2 = fraction2

    @staticmethod
    #Checks for valid input and returns one line errors for all possible cases
    def check_user_input(fraction1, fraction2, operator):
        if "/" not in fraction1 or "/" not in fraction2:
            raise Exception("Invalid fraction. Valid fractions eg 1/2, 4/5, 7/5")
        
        valid_operators = ["+","-","x","*","/"            ]
        if operator not in valid_operators:
            raise Exception("Invalid operator :( , please choose from +,-,x,*,/ ")

    @staticmethod
    def get_numerator(fraction):
        #Slicing starts at index 0 and ends at "/"
        numerator = [ int(fraction[:i]) for i in range(len(fraction)) if fraction[i] == "/" ]
        return numerator[0]

    @staticmethod
    def get_denominator(fraction):
        #The +1 starts the string slicing at the number after the / char
        denominator = [ int(fraction[i+1:]) for i in range(len(fraction)) if fraction[i] == "/"]
        return denominator[0]
    
    @classmethod
    def simplify_solution(cls, fraction):
        numerator_solution = cls.get_numerator(fraction)
        denominator_solution = cls.get_denominator(fraction)

        #Find common factors of numerator and denominator
        common_factors = [ num1 for num1 in range(1,numerator_solution) if numerator_solution % num1 == 0 and denominator_solution % num1 == 0]

        #Next divide the numerator and denominator with the highest common factor
        if len(common_factors) != 0:
            simplified_numerator = numerator_solution / max(common_factors)
            simplified_denominator = denominator_solution / max(common_factors)

        return "".join([str(int(simplified_numerator)),"/", str(int(simplified_denominator))])

    @classmethod
    def solution_of_two_fractions_based_on_operator(cls, fraction1,fraction2,operator):
        f1_numerator = cls.get_numerator(fraction1)
        f2_numerator = cls.get_numerator(fraction2)

        f1_denominator = cls.get_denominator(fraction1)
        f2_denominator = cls.get_denominator(fraction2)

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

        return "".join([str(numerator_simplify),"/", str(denominator_simplify)])

def main():
    fraction1 = input("Enter fraction here: ")
    selected_operation = input("Enter operation +,-,x,/ here: ")
    fraction2 = input("Enter second fraction here: ")

    fraction_class = FractionCalculator(fraction1, fraction2)
    fraction_class.check_user_input(fraction1,fraction2, selected_operation)

    solution = fraction_class.solution_of_two_fractions_based_on_operator(fraction1, fraction2, selected_operation)
    solution_simplified = fraction_class.simplify_solution(solution)

    print(f"Solution to its simplest form {solution_simplified}")

if __name__ == "__main__":
    main()
        