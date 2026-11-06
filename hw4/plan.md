## 1. Sketches
**Home Page**:
A text input field with past results; Nav bar at the bottom
**Result Page**:
A list of matching artworks, a filter for results, and nav bar at the bottom.
Photo of Sketch: ![alt text](IMG_8490.jpg)

## 2. API response needed
From HW3 the Art Institute of Chicago API:
- 'title'
- 'artist_title'
- 'image_id'

## 3. Specs and Checks
### `api.py`
- **What goes in (Input):** The name of the art piece
- **What comes out (Output):** The artwork's details (`title`, `artist_title`, `image_id`).
- **Checks:**
  1. Pass `"Lion (One of a Pair, South Pedestal)"` into the function, see if it returns a non-empty list of artworks.
  2. Pass a random string and see if it returns an empty list without crashing.

### `app.py`
- **What goes in (Input):** User clicks on the screen, search for an art piece, etc.
- **What comes out (Output):** Rendered HTML templates (`home.html` or `results.html`) with either the artworks or error messages.
- **Checks:**
  1. **Normal Search:** Type `water"` and click Search -> See a list of water-related artworks.
  2. **Empty Input State:** Submit the form with nothing typed -> See the message "Type a search term first."
  3. **No Results State:** Search for something that doesn't exist -> See a message like "No artworks found for __."
