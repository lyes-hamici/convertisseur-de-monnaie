from forex_python.converter import CurrencyRates , CurrencyCodes


ratio = CurrencyRates() 
symbol = CurrencyCodes()

historique = []

#Job avant pour aller plus loin
'''def convertion():
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

convertion()'''
    
def convertion_aller_plus_loin(): #Pour aller plus loin
    l = [
        'AED', 'AFN', 'ALL', 'AMD', 'ANG', 'AOA', 'ARS', 'AUD', 'AWG', 'AZN',
        'BAM', 'BBD', 'BDT', 'BGN', 'BHD', 'BIF', 'BMD', 'BND', 'BOB', 'BRL',
        'BSD', 'BTN', 'BWP', 'BYN', 'BZD', 'CAD', 'CDF', 'CHF', 'CLP', 'CNY',
        'COP', 'CRC', 'CUP', 'CVE', 'CZK', 'DJF', 'DKK', 'DOP', 'DZD', 'EGP',
        'ERN', 'ETB', 'EUR', 'FJD', 'FKP', 'FOK', 'GBP', 'GEL', 'GGP', 'GHS',
        'GIP', 'GMD', 'GNF', 'GTQ', 'GYD', 'HKD', 'HNL', 'HRK', 'HTG', 'HUF',
        'IDR', 'ILS', 'IMP', 'INR', 'IQD', 'IRR', 'ISK', 'JEP', 'JMD', 'JOD',
        'JPY', 'KES', 'KGS', 'KHR', 'KID', 'KRW', 'KWD', 'KYD', 'KZT', 'LAK',
        'LBP', 'LKR', 'LRD', 'LSL', 'LYD', 'MAD', 'MDL', 'MGA', 'MKD', 'MMK',
        'MNT', 'MOP', 'MRU', 'MUR', 'MVR', 'MWK', 'MXN', 'MYR', 'MZN', 'NAD',
        'NGN', 'NIO', 'NOK', 'NPR', 'NZD', 'OMR', 'PAB', 'PEN', 'PGK', 'PHP',
        'PKR', 'PLN', 'PYG', 'QAR', 'RON', 'RSD', 'RUB', 'RWF', 'SAR', 'SBD',
        'SCR', 'SDG', 'SEK', 'SGD', 'SHP', 'SLL', 'SOS', 'SPL', 'SRD', 'STN',
        'SVC', 'SYP', 'SZL', 'THB', 'TJS', 'TMT', 'TND', 'TOP', 'TRY', 'TTD',
        'TVD', 'TWD', 'TZS', 'UAH', 'UGX', 'USD', 'UYU', 'UZS', 'VES', 'VND',
        'VUV', 'WST', 'XAF', 'XCD', 'XDR', 'XOF', 'XPF', 'YER', 'ZAR', 'ZMW',
        'ZWD'
    ]
    somme2 = float(input("Entrer une somme d'argent à convertir : "))

    monnaie3 = str(input("Entrer la monnaie de conversion ('USD','EUR',INR, etc) : ")).upper()

    if monnaie3 not in l:
        a = str(input("Cette devise n'existe pas, voullez vous ajouter cette devise y/n : "))
        if a == "y":
            r = float(input("Qulles est le ratio de cette devise : "))
            convertion_monnaie = somme2 * r
            print("Vous avez",somme2,"",convertion_monnaie)

        if a == "n":
            print("Dans ce cas , entrer une devise existante.")
            exit()
        

convertion_aller_plus_loin()