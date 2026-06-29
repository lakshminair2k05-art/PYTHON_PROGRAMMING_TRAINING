
class VISACARD:
    def __init__(self,holder_name,card_number):
        self.holder_name=holder_name
        self.card_number=card_number
    
    def display_details(self):
        print(self.holder_name)
        print(self.card_number)
    def computer_rewards(self,purchase_type,amount):
        reward=amount*0.01
        print('the reward for the VISA is :',reward)
class HPVISACARD(VISACARD):
    def  computer_rewards(self,purchase_type,amount):
        reward=amount*0.01
        if purchase_type=="Fuel":
            reward+=10
        print('Reward for HPVISACARD is:',reward)
        #INPUT
card_type = input().strip()

if card_type not in ["VISA", "HPVISA"]:
    print("InvalidChoice")
else:
    holder_name = input().strip()
    card_number = input().strip()
    amount = float(input().strip())
    purchase_type = input().strip()

    if card_type == "VISA":
        card = VISACARD(holder_name, card_number)
    else:
        card = HPVISACARD(holder_name, card_number)

    card.display_details()
    card.computer_rewards(purchase_type, amount)

    
