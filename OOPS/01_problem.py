class Programmer:
    Employee = "microsoft"

    def __init__(self, name, product, salary):
        self.name = name
        self.product = product
        self.salary = salary

    def getinfo(self):
        print(
            f"The name of the Emplopyee is {self.name},the product is {self.product},and the salary he/she get is {self.salary}")


Subhra = Programmer("subhra", "skype", 20000)
itish = Programmer("itish", "whatsapp", 30000)
Subhra.getinfo()
itish.getinfo()