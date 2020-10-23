#start--------------------------------------

import random

print("\nZeg een zin :D")
zin = input()
leeg = ""
print("\n")
for counter in range(random.randint(3,5)):
    leeg += zin[0:random.randint(2,7)] + "... "
print(leeg + zin)

#einde--------------------------------------
