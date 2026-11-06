
## 1. Chats & Prompts 
- **Prompt 1**: "How do I structure my Flask application for HW4 and connect the Art Institute of Chicago API?"
  - **AI Response**: Suggested structuring the project into `api.py`, `app.py`, and `templates/` (home.html, results.html). Provided the API fetching logic using `requests` and how to retrieve `iiif_url` to construct the image URL (`f"{iiif_url}/{image_id}/full/843,/0/default.jpg"`).
- **Prompt 2**: "How to handle empty inputs, API errors, and missing fields in Flask?"
  - **AI Response**: Provided robust route handling in `app.py` for empty search queries, API failures (`None`), and empty result lists, along with conditional Jinja2 logic in templates.

## 2. What Surprised Me 
- When running the app initially, the page was completely blank despite that the VS Code terminal is showing 127.0.0.1 - - [06/Nov/2026 08:57:02] "GET /results?q=348y4357y3475 HTTP/1.1" 200 -
I was really confused because I didn't know what went wrong

## 3. What I Changed 
- Gemini suggested that I should go back to app.py and fix my code and make sure it looks like below:
@app.route('/results')
def show_results():
    query = request.args.get('q')
    artworks = search_art(query)
    
but I was pretty sure that my code was fine, so I tried saving the api.py and app.py again and running the web again, this time it works! Except the images still aren't showing.