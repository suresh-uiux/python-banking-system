import json, os

FILE="bank.json"

class Bank:
    def __init__(self):
        self.data=self.load()

    def load(self):
        return json.load(open(FILE)) if os.path.exists(FILE) else {}

    def save(self):
        json.dump(self.data,open(FILE,"w"),indent=4)

    def create(self):
        acc=input("Account No: ")
        pin=input("Set PIN: ")
        self.data[acc]={"pin":pin,"bal":0,"tx":[]}
        self.save()
        print("✅ Account created")

    def login(self):
        acc=input("Acc No: ")
        pin=input("PIN: ")

        if acc in self.data and self.data[acc]["pin"]==pin:
            self.menu(acc)
        else:
            print("❌ Wrong details")

    def menu(self,acc):
        while True:
            print("\n1.Deposit 2.Withdraw 3.Balance 4.History 5.Exit")
            c=input("Choose: ")

            if c=="1":
                amt=float(input("Amount: "))
                self.data[acc]["bal"]+=amt
                self.data[acc]["tx"].append(f"Deposit {amt}")

            elif c=="2":
                try:
                    amt=float(input("Amount: "))
                    if amt>self.data[acc]["bal"]:
                        raise ValueError
                    self.data[acc]["bal"]-=amt
                    self.data[acc]["tx"].append(f"Withdraw {amt}")
                except:
                    print("❌ Invalid")

            elif c=="3":
                print("Balance:",self.data[acc]["bal"])

            elif c=="4":
                print(self.data[acc]["tx"])

            else:
                self.save()
                break


bank=Bank()

while True:
    print("\n1.Create 2.Login 3.Exit")
    ch=input("Choose: ")
    if ch=="1": bank.create()
    elif ch=="2": bank.login()
    else: break
