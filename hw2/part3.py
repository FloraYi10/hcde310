# HW2 Part 3 – Counting with a dictionary
#
# In `part3.py`:
#
# 1. Build a dictionary counting works per artist, and print it: `{'Vincent van Gogh': 1, ...}`. A
#    work with no artist counts under `'Unknown'`.
# 2. Print the artist with the most works: `Most works: Claude Monet (2)`
#
# (This is the letter-counting pattern from Class 3, applied to art.)

from artworks import artworks

counts = {}
for art in artworks:
    artist = art.get("artist", "Unknown")
    counts[artist] = counts.get(artist, 0) + 1

print(counts)

name_of_most= ""
most_count = 0

for artist in counts:
    if counts[artist] > most_count:
        name_of_most = artist
        most_count = counts[artist]
print(f"Most works: {name_of_most} ({most_count})")
