from pathlib import Path

p = Path("/mnt/c/EQLite/Logs/eqlog_Sanguinne_P1999Green.txt")

# Test path
# p = Path("/home/sanguine/workspace/arcanum/watcher/README.md")

# Actual windows path
# "C:\EQLite\Logs\eqlog_Gottfred_P1999Green.txt"

# print(p.read_text())

# print(p.is_dir())


phrase = "train"
# monster = " Guard Eaglesong"

matches = []
count = 0

with p.open() as f:
    for line in f:
        if phrase.lower() in line.lower():
            matches.append(line.rstrip())
            count += 1

print(matches)
print(count)
