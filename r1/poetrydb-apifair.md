# PoetryDB API Fair

## 1. What it is & Why a Designer Might Care
A public API that provides a wide range of poetry and author metadata, returning results in JSON or text formats. It allows query poems by author, title, specific lines, line count, and even fetch author biographies.
 

**Why a designer cares:** Designers can prototype content-heavy editorial interfaces like quote widgets or narrative-driven games without spending hours manually curating copy or building a custom database.

## 2. Setup & Authentication
- **Authentication:** No API key required
- **Installation:** No special installation or SDK needed. You can query it directly using standard HTTP `fetch` in JavaScript or the `requests` library in Python.
- **Base URL:** `https://poetrydb.org`

## 3. Working Example (Code + Output)

Fetching lines from "Ozymandias":

```python
import requests

url = "https://poetrydb.org/title/Ozymandias/lines.json"
response = requests.get(url)
data = response.json()

# PoetryDB always returns a list. Access the first element [0] to get the poem data.
poem = data[0]

# Print the first three lines
for line in poem['lines'][:3]:
    print(line)
```

**Output:**
```text
I met a traveller from an antique land
Who said: Two vast and trunkless legs of stone
Stand in the desert... Near them, on the sand,
```
## 4. Gotchas


- Language Limitations: The dataset primarily focuses on English-language poetry; it currently lacks metadata for poems in other languages.
- Error Handling: If a title or author query doesn't match an exact string in the database, the API returns a simple status message or empty array rather than a 404 error.

## 5. Design Angle

- Project Idea: An ambient lock screen widget or minimalist web extension that fetches a random classical poem line every day.
- Ethical / UX Consideration: Typography needs to be flexible based on text length, so long text blocks don't break the layout or look messed up.

AI Disclosure: AI was used to assist in organizing and polishing the structure of this guide. All code snippets have been tested and verified locally.