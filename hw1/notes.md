# HW1 notes

## Part 4: Predict, run, explain

**My prediction for `predict.py` (written BEFORE running it):**
0 The Bedroom 1989
1 Nighthawks 2042
2 American Gothic 2030
9
10

**What it actually printed:**
0 The Bedroom 1989
1 Nighthawks 2042
2 American Gothic 2030
10
11

**Explain:** If I was off, which line surprised me and why? If I was right, why do the last two lines print different numbers?

My Prediction was off on the last two lines.
I predicted 9 and 10, but the real output was 10 and 11. I predicted (len(titles)) as 9 because I was thinking of the last index. Python starts counting at 0, so the last title is titles[9], while there are 10 titles in total.
I predicted print(len(titles[0])) as 10 because I counted the letters in "The Bedroom" but skipped the space.


## Part 5: Reflection (about 100 words)

Look back at your Day 1 app: its code if you can still open it, or your screenshots of it running. Is there anything you can now recognize (a loop, an `if`, a list)? Where? If you only have screenshots, what do you think the code had to do to make the app behave that way?

As I was looking back at my Day 1 screenshot, there were several elements that remind me of the code I wrote in this assignment. I recognized that the artwork cards looks like the for loop in part 2, because each image has the same format, just with different image and titles. The pinterest-style category tabs also reminds me of the if statement in "years[i]>cutoff" in part 3. By selecting certain category(Photography, Sculpture, etc), the results are only filtered down to the ones that fits that specific requirements.