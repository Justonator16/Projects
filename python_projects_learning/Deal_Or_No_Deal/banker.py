import random 
import time
#Looks at avaialbe amounts and offers an amount to buy player box
def banker_offer(boxes_available: dict ):
    amounts = boxes_available.values()

    sum_of_amounts = 0
    for amount in amounts:
        sum_of_amounts += amount

    banker_offer = sum_of_amounts / len(amounts)
    print(f"The banker is offering R{banker_offer} to buy your box.")
    deal_or_no_deal = input("Deal or No Deal ? ")
    if deal_or_no_deal.lower() == "deal" or "d" in deal_or_no_deal.lower() :
        print("Congratulations you won R{banker_offer}")
        print("Thanks for playing my deal or no deal game . I hope the banker didnt give you a hard time :)")
        quit()
    elif "n" in deal_or_no_deal.lower() :
        print("Ohh No deal , Well lets continue to the next round.")
        time.sleep(3)

    return banker_offer
    