
from flask import Flask, render_template, request
from api import search_art

app = Flask(__name__)

# Step-by-step plan (Pseudocode):
# 1. When the user visits the home page ("/"), show the search box page (home.html).
# 2. When the user searches, go to the results page ("/results").
# 3. Get what the user typed from the search box.
# 4. If the box is empty, show "Type a search term first."
# 5. If the box is not empty, use function in api.py to get art data from the internet.
# 6. Check if the internet/API is broken or if there are zero results. If so, show "No artworks found for__".
# 7. If everything is good, show the list of artworks on the results page (results.html).

@app.route("/") # AI Written
def home():
    return render_template("home.html")

@app.route("/results") # AI Written
def results():
    # Get the user's search text and remove extra spaces
    query = request.args.get("q", "").strip()

    # Situation 1: If the box is empty, show "Type a search term first.
    if query == "":
        return render_template("home.html", message="Type a search term first.")

    # Call api.py to get art data
    artworks = search_art(query)

    # Situation 2: If the API failed or internet is down (returns None)
    if artworks is None:
        return render_template("results.html", message="The art database is not responding. Please try again.")

    # Situation 3: If found nothing (empty list)
    if len(artworks) == 0:
        return render_template("results.html", message=f"No artworks found for '{query}'.")

    # Normal case: Show the artworks
    return render_template("results.html", artworks=artworks, query=query)
# AI Written
if __name__ == "__main__": 
    app.run(debug=True)

#When I ran it, the site did not show the actual image, more like just placeholders for all the images