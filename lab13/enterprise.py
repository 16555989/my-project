
class ENTERPRISE:
    def __init__(self, name, finance, year, owner):
        self.Name = name
        self.Finance = finance
        self.Year = year
        self.Owner = owner

    def SetFinance(self, finance):
        self.Finance = finance

    def GetFinance(self):
        return self.Finance

    def DisplayAll(self):
        print("Назва:", self.Name)
        print("Активи (тис. грн):", self.Finance)
        print("Рік створення:", self.Year)
        print("Власник:", self.Owner)

    def SetOwner(self, owner):
        self.Owner = owner

    def GetOwner(self):
        return self.Owner
