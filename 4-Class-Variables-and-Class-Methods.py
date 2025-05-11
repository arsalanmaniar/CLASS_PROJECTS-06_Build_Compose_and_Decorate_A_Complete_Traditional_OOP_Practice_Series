class Bank:
    bank_name = "HBL Bank"  # Class variable

    def __init__(self, account_holder):
        self.account_holder = account_holder

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name
    
    def display(self):
        print(f"Account Holder: {self.account_holder}, Bank Name: {self.bank_name}")
 
account1 = Bank("Arsalan")
account2 = Bank("Ali")

account1.display()
account2.display()

Bank.change_bank_name("Meezan Bank")

account1.display()
account2.display()