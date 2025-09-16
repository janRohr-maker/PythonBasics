# Block 1 Aufgabe 6

preis = 3.20
geld = 20.00
anzahl_der_Riegel = int(geld // preis)
rest_geld = geld % preis
print(f"Riegel kaufen: {anzahl_der_Riegel}, Restgeld: {rest_geld:.2f} CHF")