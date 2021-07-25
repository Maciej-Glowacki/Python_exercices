class BankAccount:
    def __init__(self, number):
        self.number = number
        self.cash = 0.0


    def deposit_cash(self, amount):
        if not isinstance(amount, float) and amount <= 0.0:
            raise ValueError("Deposit can't be negative!")
        self.cash += amount
    
    
    def withdraw_cash(self,amount):
        if amount < 0.0:
            raise ValueError("Withdraw can't be negative")
        self.cash -= min(self.cash, amount)
        
        
    def __str__(self):
        return f'Account: {self.number}, balance: {self.cash}'

myaccount = BankAccount(1496454578)
print(myaccount)
myaccount.deposit_cash(429)
print(myaccount)
myaccount.deposit_cash(156)
print(myaccount)
myaccount.withdraw_cash(1000)
print(myaccount)

# Mieć atrybuty:
# number - atrubyt ten powinien trzymać numer identyfikacyjny konta (dla uproszczenia możemy założyć, że numerem konta może być dowolna liczba całkowita),
# cash - atrybut określający ilość pieniędzy na koncie. Ma to być liczba zmiennoprzecinkowa.
# Posiadać konstruktor przyjmujący tylko numer konta. Atrybut cash powinien być zawsze nastawiany na 0.0 dla nowo tworzonego konta.
# Posiadać metodę deposit_cash(amount) której rolą będzie zwiększenie wartości atrybutu cash o podaną watość. Pamiętaj o sprawdzeniu czy podana wartość jest większa od 0.0
# Posiadać metodę withdraw_cash(amount) której rolą będzie zmniejszenie wartości atrybutu cash o podaną watość. Metoda ta powinna zwracać ilość wypłaconych pieniędzy. Dla uproszczenia zakładamy że ilośc pieniędzy na koncie nie może zejść poniżej 0.0, np. jeżeli z konta na którym jest 300zł próbujemy wypłacić 500zł to metoda zwroci nam tylko 300zł. Pamiętaj o sprawdzeniu czy podana wartość jest większa od 0.0.
# Posiadać metodę print_info() nie przyjmującą żadnych parametrów. Metoda ta ma wyświetlić informację o numerze konta i jego stanie.