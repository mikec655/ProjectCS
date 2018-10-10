#opdracht 8

T = int(input("geef de temperatuur op in graden celsius:"))

B = int(input("geef de windsnelheid op kilometer per uur:"))

G = (13 + 0.62*T - 14*B**0.24 + 0.47*T*B**0.24)

print (G)
