from forex_python.converter import CurrencyRates , CurrencyCodes


ratio = CurrencyRates() 
symbol = CurrencyCodes()

historique = []


def convertion():
    chaine =""
    try:

        print("----------------------------------------")

        somme = float(input("Entrer une somme d'argent à convertir : "))

        print("----------------------------------------")

        monnaie1 = str(input("Entrer une monnaie à convertir ('USD','EUR',INR, etc) : ")).upper()

        print("----------------------------------------")

        monnaie2 = str(input("Entrer la monnaie de conversion ('USD','EUR',INR, etc) : ")).upper()

        print("----------------------------------------")
    
        devise1 =  symbol.get_symbol(monnaie1)
        devise2 =  symbol.get_symbol(monnaie2)



        convertion_monnaie = ratio.convert(str(monnaie1), str(monnaie2),somme)
        chaine += str(somme)
        chaine += " "
        chaine += str(monnaie1)
        chaine += " converti en "
        chaine += str(monnaie2)
        chaine += " = "
        chaine += str(convertion_monnaie)
        chaine += " "
        chaine += str(monnaie2)


    except Exception as e :
        print("Monnaie inconnue où n'existe pas.")
        exit()

    historique.append(chaine)
    print(somme,devise1,"converti en ",devise2," = ",convertion_monnaie," ",devise2)

    print("----------------------------------------")

    print("Historique :",historique)

    fichier = open("historique.txt", "a")
    fichier.write("\n" + chaine + "\n")
    fichier.close()
    





convertion()