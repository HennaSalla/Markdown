# MUUTUJAT MERKKIJONOSSA
# ======================

# Sanakirjat
henkilo1 = {'etunimi': 'Tiina', 'ika': 27}
henkilo2 = {'etunimi': 'Jaana', 'ika': 44}
henkilo3 = {'etunimi': 'Iida', 'ika': 7}

# Perinteinen ratkaisu
print(henkilo1['etunimi'] + 'n', 'ikä on', henkilo1['ika'], 'vuotta')

# Samaa muotoilua merkkijonona (fstring)

muotoilu_merkkijono = f'{henkilo1["etunimi"]}n ikä on {henkilo1["ika"]} vuotta'
print(muotoilu_merkkijono)