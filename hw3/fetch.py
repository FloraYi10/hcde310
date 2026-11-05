# HW3 Part 2 + Part 3 + Part 4
#
# Instructions: README.md in this folder (same as the assignment on Canvas).

import requests

FIELDS = "id,title,artist_title,artist_display,date_display,department_title"

# Functions go here (above the code that runs)
def count_by_artist(artworks):
    """Takes a list of artworks and returns a dictionary of artist-artwork counts."""
    counts = {}
    for art in artworks:
        artist = art["artist_title"] or "Unknown"
        counts[artist] = counts.get(artist, 0) + 1
    return counts

def save_results(artworks, filename):
    with open(filename, "w", encoding="utf-8") as f:
        for art in artworks:
            title = art["title"]
            artist = art["artist_title"] or "Unknown artist"
            date = art["date_display"] or "Unknown date"
            f.write(f"{title} | {artist} | {date}\n")


term = input("Search the Art Institute for: ")
url = "https://api.artic.edu/api/v1/artworks/search"      # TODO: the search URL from step 2
params = {"q": term, "fields": FIELDS}   # TODO: q (the search term) and fields (FIELDS)
headers = {"AIC-User-Agent": "HCDE310 student project"}
response = requests.get(url, params=params, headers=headers)

# TODO step 3: check response.status_code before you use the data
if response.status_code !=200:
    print(f"Sorry, something went wrong: {response.status_code} {response.reason}")
else:
    data = response.json()
    results = data["data"]
    if not results:
        print(f"No results found for '{term}'. Try a different search term.")
    else:
        for art in results:
            title = art["title"]
            artist = art["artist_title"] or "Unknown artist"
            date = art["date_display"] or "Unknown date"
            department = art["department_title"] or "Unknown department"
            print(f"{title} - {artist} ({date})")
            print(f"    Department: {department}")

        counts = count_by_artist(results)
        filename = f"{term}_results.txt"
        save_results(results,filename)
        print(f"Saved{len(results)} results to {filename}")
        for artist, n in counts.items():
            print(f"{artist}:{n}")