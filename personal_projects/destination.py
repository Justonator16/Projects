def get_number_of_house(user_input):
    # Returns a list of number 0 to 9 in string format
    number_list = [ str(i) for i in range(0,10)]

    num_houses = []
    for i in range(len(user_input)):
        if user_input[i] in number_list:
            num_houses.append(user_input[i])
        else: 
            break
    
    return "".join(num_houses)

def get_budget(user_input):
    length_of_house_indexes = len(get_number_of_house(user_input=user_input))
    budget = user_input[length_of_house_indexes+1:]
    return budget

def get_house_price(houses_price):
    number_list = [ str(i) for i in range(0,10)]
    index_of_spaces = [ i for i in  range(len(houses_price)) if i not in number_list]
    
    house_prices = []
    for i in range(len(houses_price)):
        for index in range(len(index_of_spaces)):
            if index == 0:
                house_prices.append(house_prices[:index_of_spaces[index]])
            elif index+1 < len(index_of_spaces):
                house_prices.append(house_prices[index_of_spaces[index]:index_of_spaces[index+1]])
            else:
                house_prices.append(houses_price[:index_of_spaces[index]])
    return house_prices

user_input = input("Enter number of houses and budget: ")
houses_price = input("Enter price for each house: ")


print(get_number_of_house(houses_price))

