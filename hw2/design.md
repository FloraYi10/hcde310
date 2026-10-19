# HW2 Part 1 – Model first (in `design.md`, no code)

---

## 1. Why is `artworks` a list of dictionaries and not one big dictionary? What would you lose or gain the other way?
If 'artworks' is a big dictionary instead of a list of dictionaries, I wouldn't be able to search for a specific art piece by its order. However, if I use a big dictionary and use the title as the key of each piece, then I can easily search by titles. 

## 2. Which fields are sometimes missing? What should the app show when they are?
For pieces like "Nighthawks", "The Old Guitarist", "The Child's Bath", "Sky above Clouds IV", and "Stacks of Wheat(End of Summer)", the list did not provide their mediums; "The Child's Bath" did not provide its year of creation; and for Untitled(vase), the list only included its title.

The app should show the users that the specific information is unknown when something is missing.