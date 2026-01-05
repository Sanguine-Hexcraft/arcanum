
from pathlib import Path            # Import Path for working with filesystem paths
import time                         # Import time for sleeping between checks
from pydub import AudioSegment     # Import pydub to play audio alerts
import subprocess

# Path to the file we want to watch.
p = Path("/mnt/c/EQLite/Logs/eqlog_Marthus_P1999Green.txt")

# The line of text we want to watch for
phrase = "Your charm spell has worn off."

# Path to a sound file to play when the phrase appears
sound_file = "./audio/Clarity.wav"
sound = AudioSegment.from_file(sound_file)

with p.open() as f:                 # Open the log file for reading
    f.seek(0, 2)                    # Move the file pointer to the end (ignore old lines)

    
    print("Watching for Charm Break")

    while True:                     # Run forver and ever and ever...
        line = f.readline()         # Read the next line added to the file

        if not line:                # If no new line is available yet
            time.sleep(0.2)         # Pause briefly to avoid busy-waiting
            continue                # Go back to the top of the loop
        
        if phrase.lower() in line.lower():
            print("MATCH:", line.rstrip())

            # Explicit ffplay call (cross-platform)
            subprocess.run([
                "ffplay",
                "-nodisp",   # no video window
                "-autoexit", # exit after playing
                str(sound_file)
            ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
