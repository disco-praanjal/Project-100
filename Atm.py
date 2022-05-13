class ATM(object):

    def __init__(self, card_number, pin_number):
        self.card_number=card_number
        self.pin_number=pin_number

    def CashWidraw(self):
        print("cashWidrawed")
        "How much cash is to be widrawed ?"

    def BalanceEnquiry(self):
        print("balanceEnquired")
        "What is your balence querry ?"
        
Custumor = ATM("123456789", "12345")

print(Custumor.CashWidraw())
print(Custumor.BalanceEnquiry())