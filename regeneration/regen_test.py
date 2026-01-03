#
#implement pygame solution later

import time

regen_toggle = False
hp = 100
mana = 100

# Text part of the simulation
#
#
print("++++++")
print("Welcome Adventurer")
print("++++++")


print("++++++")
print(f"Your Current hp is {hp}/200")
print("++++++")


print("++++++")
print(f"Your current mana is {mana}/200")
print("++++++")




key = input("Press (x) to sit and regen: ")
if key.lower() == "x":
    regen_toggle = True



while regen_toggle is True:
    hp += 10
    mana += 10

    if hp == 200 or mana == 200:
        regen_toggle = False

    print(f"Your {hp}(Hitpoints), Your {mana}(Mana)")
   
    time.sleep(1)

