# Definieer de dictionary met prijzen van verschillende ijssmaken
prijzen = {
    'aardbei': 3,
    'vanille': 4,
    'chocolade': 5
}

# Bereken de prijs van vanille-ijs met een korting van 20%
aanbieding = prijzen['vanille'] * 0.8

# Maak een geformatteerde tekst met de aanbieding
reclame_tekst = f"Vandaag in de aanbieding: vanille-ijs, 1 liter – slechts € {aanbieding:.2f}"

# Vind de index van de eerste nul na de komma in de prijsaanduiding
index_eerste_nul = reclame_tekst.index('0', reclame_tekst.index('€') + 1)

# Maak een nieuwe tekst zonder de eerste nul na de komma
reclame_tekst2 = reclame_tekst[:index_eerste_nul] + reclame_tekst[index_eerste_nul + 1:]

# Zet de reclametekst om naar hoofdletters indien het woord 5 of meer karakters heeft
# Anders zet het woord om naar kleine letters
for woord in reclame_tekst2.split():
    if len(woord) >= 5:
        print(woord.upper())
    else:
        print(woord.lower())
