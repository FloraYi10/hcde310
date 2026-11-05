# HW3 Part 1 – Read the response first

AI Use: Stage 2 (Tutor)

Open `sample_response.json` (a saved Art Institute of Chicago search). In `notes.md`:

---

## 1. The total number of results is at `data["pagination"]["total"]`. What's the path to the first artwork's title?
data["data"][0]["title"]

## 2. Find 3 more fields you'd want to show a user, and their paths
- data["data"][0]["artist_title"]
- data["data"][0]["date_display"]
- data["data"][0]["department_title"]

## 3. Which fields are `null` for some works?
- data["data"][2]["artist_title"]is null

## 4. Predict
*open `fetch.py` and read it, but don't change anything yet. What do you think will happen when you run it?*
I think the program will crash at the 'requests.get(url, params=params)' line, because "" is not a valid url.

## 5. Run it
*run `python3 fetch.py`. When it asks for a search term, type a word (like `cat`) and press Enter. What actually happened? Read the traceback bottom line first: what went wrong, and which line of your file caused it?*
When I typed cat, it returned requests.exceptions.MissingSchema: Invalid URL '': No scheme supplied.

I think it is because the url was still "" since I didn't fill in the TODO from the line `response = requests.get(url, params=params)` in fetch.py 