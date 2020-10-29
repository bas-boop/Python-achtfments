
print("\nWelkom bij dagelijke keuzes! Nu ga je een paar vragen beantwoorden.")

def vraag6():
    print("vraag 6: wat ga je drinken?")
    print("Koffie, melk, sap of niks")
    antwoord5 = input()
    if antwoord5 == "koffie":
        print("KOFFIE")
        return
    elif antwoord5 == "melk":
        print("melk is goed voor elk")
        return
    elif antwoord5 == "sap":
        print("sap is raar voor eerst drinken, mijn mening")
        return
    elif antwoord5 == "niks":
        print("Waarom drink je niks")
        return
    else:
        print("Kies chocola of rozijen.")
        vraag5()

def vraag5():
    print("Vraag 5: Welke muslie wil je?")
    print("chocola of rozijen")
    antwoord5 = input()
    if antwoord5 == "chocola":
        print("Dat is wel lekker.")
        vraag6()
    elif antwoord5 == "rozijen":
        print("Dat is lekker gezond.")
        vraag6()
    else:
        print("Kies chocola of rozijen.")
        vraag5()

def vraag4():
    print("Vraag 4: Wat wil je op je brood?")
    print("hagelslag, kaas, ham, pindakaas, jam, gehakt, ei, suker, worst, chocola, fruit, avondeten, brood of boter?")
    antwoord4 = input()
    if antwoord4 == "hagelslag":
        print("Lekker zoet")
        vraag6()
    elif antwoord4 == "kaas":
        print("Lekker hardtig")
        vraag6()
    elif antwoord4 == "ham":
        print("Lekker hardtig")
        vraag6()
    elif antwoord4 == "pindakaas":
        print("Lekker zoet")
        vraag6()
    elif antwoord4 == "jam":
        print("Lekker zoet")
        vraag6()
    elif antwoord4 == "gehakt":
        print("Lekker hardtig")
        vraag6()
    elif antwoord4 == "ei":
        print("Lekker hardtig")
        vraag6()
    elif antwoord4 == "suiker":
        print("Lekker zoet")
        vraag6()
    elif antwoord4 == "worst":
        print("Lekker hardtig")
        vraag6()
    elif antwoord4 == "chocola":
        print("Lekker zoet")
        vraag6()
    elif antwoord4 == "fruit":
        print("Lekker zoet")
        vraag6()
    elif antwoord4 == "frituur":
        print("Lekker hardtig")
        vraag6()
    elif antwoord4 == "avondeten":
        print("Lekker hardtig")
        vraag6()
    elif antwoord4 == "brood":
        print("Lekker zoet")
        vraag6()
    elif antwoord4 == "boter":
        print("idk of dit zoet of hartig is.")
        vraag6()
    else:
        print("Je moet wel een antwoord kiezen want ik kan niet elk eten hier neer zetten.")
        vraag4()

def vraag3():
    print("Vraag 3: Wil je nu wel opstaan?")
    print("Ja of nee?")
    antwoord3 = input()
    if antwoord3 == "ja":
        print("Ga dan nu ontbijten")
        vraag2()
    elif antwoord3 == "nee":
        print("slaap lekker alweer")
        return
    else:
        print("Je mag alleen ja of nee typen.")
        vraag3()

def vraag2():
    print("\nVraag 2: Wat wil je voor ontbijt?")
    print("brood, muslie of niks")
    antwoord2 = input()
    if antwoord2 == "brood":
        print("klinkt lekker")
        vraag4()
    elif antwoord2 == "muslie":
        print("Goede keuze")
        vraag5()
    elif antwoord2 == "niks":
        print("Waarom wil je geen ontbijt")
        vraag6()
    else:
        print("Je mag alleen kiezen uit brood, muslie of niks")
        vraag2()

def vraag1():

    print("\nVraag 1: uit slapen of niet?")
    print("ja of nee?")
    antwoord1 = input()
    if antwoord1 == "ja":
        print("Slaap lekker")
        vraag3()
    elif antwoord1 == "nee":
        print("Waarom slaap je niet uit.")
        vraag2()
    else:
        print("Je mag alleen ja of nee typen.")
        vraag1()
vraag1()

print("\nDit was jou dagelijke leven.\nEinde code!")
