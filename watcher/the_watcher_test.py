from pathlib import Path

p = Path("/mnt/c/EQLite/Logs/eqlog_Sanguinne_P1999Green.txt")


phrase = "Your charm spell has worn off."


matches = []
count = 0

with p.open() as f:
    for line in f:
        if phrase.lower() in line.lower():
            matches.append(line.rstrip())
            count += 1


for i, line in enumerate(matches, start=1):
    print(f"{i:>4}: {line}")

print(f"\nMatches for '{phrase}' ({count} Total):\n")
