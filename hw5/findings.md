# HW5 findings

## 1. Drawing: one search for "Monet"
![Box and Arrow Sketch](../Box%20and%20Arrow%20Sketch.jpg)

## 2. Two questions about the code
1. Why put def home(): after @app.route("/")? What does it do?
2. For app.run(debug=True) does it mean whenever it passes this step, the app works? 

## 3. Checks (4 or more, at least 2 as pytest tests)
| # | Check | Pass or fail |
| 1 | Searching for a valid artist name  returns the result page with a 200 OK status code|Pass|
| 2 |Inputting a real artist's name that has no artworks in the museum's API returns a no-result message rather than crashing |Pass|
| 3 | Submitting an empty search form or random characters will reminds the user to enter a valid input |Fail|
| 4 |The root URL (/) loads correctly and displays the search frame with a 200 OK status code.|Pass|

## 4. AI review
What it found that I missed:
It found that I am missing an input validation, which means the app will just pass an empty string to the API without checking; it also found that app.py lacks error handling, which would cause a 500 Internal Server Error if the external API goes down or time out.
What it got wrong:
The AI review sometimes suggests things we don't need for our app like user authentication.

Answers to my two questions:

1. Why put def home(): after @app.route("/")? What does it do?

The @app.route("/") tells Flask that whenever a user visits the root URL (/), it should execute the def home() function right away. 

2. For app.run(debug=True) does it mean whenever it passes this step, the app works? 

No, app.run(debug=True) simply exists to start the local Flask development server and turns on debug mode

## 5. My fix
What was wrong:The app lacked input validation. If a user submitted a blank space, the app would pass it directly into the API request.

What I changed:In app.py, I updated the empty-input check inside the /results route to return prompt "Please enter a valid artist name."
How I checked it works:Ran the Flask app with a blank search, and confirmed the updated prompt displayed properly on home.html with python3 -m pytest.

Commit before: (0d5bb08)  Commit after: (6108636)

## 6. Can we ship it? (100–150 words)
Yes or no, and why:
No, we should not ship this app tomorrow. The app still has no input validation for empty search queries or random input. I believe that the user experience would be pretty bad if we just ship it since it is only ready for inputs that matches what's in the museum API.

One thing my HW4 does better:
My HW4 app includes comprehensive error handling and input verification, ensuring that users receive clear, friendly feedback when searches fail or inputs are invalid.

One thing the AI's app does better:
The AI's app utilizes clean, modern CSS styling and a more concise, modular template structure, the initial layout also looks pretty minimal.

AI use goes in `ai_use.md` (the five points on the AI Use Card).
