# Klasa sklepu internetowego- atrybuty:
#
# Konstruktor domyslny - zaczynamy od braku danych,
# dopiero w trakcie dzialania sklepu beda one dodawane
# clients - liczba klientow odwiedzajacych sklep (w danej chwili)
# prod1 - liczb produktow wyswietlonych
# prod2 - liczba produktow dodanych do koszyka
# prod3 - liczba produktow, ktore zostaly sprzedane
# performance - wydajnosc serwera :

# Wydajnosc zalezy od wielu czynnikow, np: liczby odwiedzajacych, ilosci produktow w sklepie,
# Mozna zalozyc jakas liczbe na poczatek np 80 i zwiekszac ja np w momencie wiekszej liczby klientow na stronie
# Albo w momencie
# Zakladamy, ze strona internetowa jest postawiona na dwoch serwerach, zatem:

# runServers (running servers) - liczba oznaczajaca dzialajace serwery - na poczatku 2
# W trakcie dzialania programu ta liczba moze ulec zmianie, poniewaz ktorys z serwerow mogl ulec awarii
# Ilosc dzialacych serwerow bedzie wplywala na wydajnosc
# error - numer/rodzaj awarii/bledu na serwerze
# repairTime - w zaleznosci od tego, jaki blad wystapil - czas naprawy bedzie rowny
# speed - predkosc [%]

class Shop:
    def __init__(self, clients=0, prod1=0, prod2=0, prod3=0, performance=80, runServers=2, error=0, repairTime=0, speed=100):
        self.clients = clients
        self.prod1 = prod1
        self.prod2 = prod2
        self.prod3 = prod3
        self.performance = performance
        self.runServers = runServers
        self.error = error
        self.repairTime = repairTime
        self.speed = speed