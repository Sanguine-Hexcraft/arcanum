import time

hp = 100
mana = 100
MAX = 200

is_sitting = True

print("Welcome Adventurer")

while True:
    print(f"\nHP: {hp}/{MAX} | Mana: {mana}/{MAX}")
    print("Press (x) to sit / stand")
    print("Press (q) to quit")

    key = input("> ").lower()

    if key == "q":
        print("Goodbye hero.")
        break

    if key == "x":
        is_sitting = not is_sitting
        state = "sitting and meditating" if is_sitting else "standing"
        print(f"You are now {state}.")

    # regen tick (1 second)
    if is_sitting:
        hp = min(hp + 10, MAX)
        mana = min(mana + 10, MAX)
        print("You regenerate...")

    time.sleep(1)    
