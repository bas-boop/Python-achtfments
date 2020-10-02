#appels
print("\n")

print("333 appelbomen")
print("2/3 schaduw 20% minder dan zon (80%)")
print("146 appels per boom zon")
print("3 eigenaars, dus alle appels delen door 3\n")

bomen = 333
bomenZ = bomen / 3
bomenS = bomen / 3 * 2
print("Wat zijn de aantal bomen in de zon: " + str(bomenZ))
print("Wat zijn de aantal bomen in de schaduw: " + str(bomenS))
print("\n")

appelsZ = 146
appelsS = appelsZ * 0.8
print("Hoeveel appels geeft een zonnige boom: " + str(appelsZ))
print("Hoeveel appels geeft een schaduw boom: " + str(appelsS))
print("\n")

BAZ = appelsZ * bomenZ
BAS = appelsS * bomenS
AA = BAZ + BAS

print("Hoeveel appels geven alle zonnige bomen: " + str(BAZ))
print("Hoeveel appels geven alle schaduw bomen: " + str(BAS))
print("Hoeveel appels geven alle bomen: " + str(AA))
print("\n")

AAA = AA % 3
B = AA - AAA

print("Jullie mogen allemaal " + str(B) + " appels verkopen.")
print("De gesneden appels mogen jullie lekker op eten :D , geniet er van (" + str(AAA) + ").")

print("\n")
