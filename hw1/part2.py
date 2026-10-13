# HW1 Part 2: Lists and loops
# Run it:  python3 part2.py
# Your output must match expected/part2.txt exactly.

from artworks import titles
number = 1
for t in titles:
    print(f"{number}. {t}")
    number = number +1
print(f"Titles: {len(titles)}")

count = 0
for t in titles:
    if "a" in t.lower():
        count = count + 1
print(f'Titles with an "a": {count}')

longest = ""
for t in titles:
    if len(t) > len(longest):
        longest = t
print(f"Longest: {longest}")




