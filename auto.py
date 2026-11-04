
modellen = {
    "City": 22500,
    "Comfort": 32500,
    "Sport": 42500
}

motoren = {
    "Benzine": 0,
    "Hybride": 4000,
    "Elektrisch": 7500
}

kleuren = {
    "Rood": 500,
    "Groen": 650,
    "Geel": 750,
    "Oranje": 600
}

uitvoeringen = {
    "Standard": 0,
    "Comfort": 1500,
    "Premium": 3000
}

extra_opties = {
    "Navigatie": 500,
    "Panoramadak": 1200,
    "Sportvelgen": 800,
    "Stoelverwarming": 400
}


while True:
    print("Welkom bij Autofactory!")
    print("1. Nieuwe auto samenstellen")
    print("2. Opgeslagen auto's bekijken")
    print("3. Programma afsluiten")

    keuze = input("Kies een optie: ")

    if keuze == "1":
        print("Nieuwe auto samenstellen")

        for model, prijs in modellen.items():
            print(f"{model} - €{prijs}")

        model_keuze = input("Kies een model: ")

        if model_keuze in modellen:
            print("Kies een motortype:")

            for motor, prijs in motoren.items():
                print(f"{motor} - €{prijs}")

            motor_keuze = input("Kies een motor: ")

            if motor_keuze in motoren:
                print("Kies een kleur:")

                for kleur, prijs in kleuren.items():
                    print(f"{kleur} - €{prijs}")

                kleur_keuze = input("Kies een kleur: ")

                if kleur_keuze in kleuren:
                    print("Kies een uitvoering:")

                    for uitvoering, prijs in uitvoeringen.items():
                        print(f"{uitvoering} - €{prijs}")

                    uitvoering_keuze = input("Kies een uitvoering: ")

                    if uitvoering_keuze in uitvoeringen:

                        gekozen_extras = []

                        print("Kies extra opties of typ Klaar:")

                        for extra, prijs in extra_opties.items():
                            print(f"{extra} - €{prijs}")

                        extra_keuze = input("Kies een extra optie: ")

                        while extra_keuze != "Klaar":
                            if extra_keuze in extra_opties:
                                if extra_keuze not in gekozen_extras:
                                    gekozen_extras.append(extra_keuze)
                                    print("Optie toegevoegd.")
                                else:
                                    print("Deze optie is al gekozen.")
                            else:
                                print("Ongeldige keuze.")

                            extra_keuze = input("Kies nog een optie of typ Klaar: ")

                        totaal_prijs = (
                            modellen[model_keuze]
                            + motoren[motor_keuze]
                            + kleuren[kleur_keuze]
                            + uitvoeringen[uitvoering_keuze]
                        )

                        for extra in gekozen_extras:
                            totaal_prijs = totaal_prijs + extra_opties[extra]

                        print("\n--- Jouw auto ---")
                        print(f"Model: {model_keuze}")
                        print(f"Motor: {motor_keuze}")
                        print(f"Kleur: {kleur_keuze}")
                        print(f"Uitvoering: {uitvoering_keuze}")
                        print(f"Extra opties: {gekozen_extras}")
                        print(f"Totaalprijs: €{totaal_prijs:,}".replace(",", "."))

                        opslaan = input("Wil je deze auto opslaan? ja/nee: ")

                        if opslaan == "ja":
                            with open("configuraties.txt", "a") as bestand:
                                bestand.write("\nNieuwe auto:\n")
                                bestand.write(f"Model: {model_keuze}\n")
                                bestand.write(f"Motor: {motor_keuze}\n")
                                bestand.write(f"Kleur: {kleur_keuze}\n")
                                bestand.write(f"Uitvoering: {uitvoering_keuze}\n")
                                bestand.write(f"Extra opties: {gekozen_extras}\n")
                                bestand.write(f"Totaalprijs: €{totaal_prijs}\n")

                            print("Auto opgeslagen!")

                        else:
                            print("Auto niet opgeslagen.")

                    else:
                        print("Ongeldige uitvoering.")

                else:
                    print("Ongeldige kleur.")

            else:
                print("Ongeldige motor.")

        else:
            print("Ongeldig model. Probeer opnieuw.")

    elif keuze == "2":
        print("Opgeslagen auto's:")

        try:
            with open("configuraties.txt", "r") as bestand:
                print(bestand.read())

        except FileNotFoundError:
            print("Er zijn nog geen auto's opgeslagen.")

    elif keuze == "3":
        print("Programma afsluiten")
        break

    else:
        print("Ongeldige keuze. Probeer opnieuw.")