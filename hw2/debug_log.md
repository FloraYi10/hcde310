# HW2 Part 5 – Debug log (`debug_log.md`)

Record **at least 2 errors** you hit. No errors? Break something on purpose and log it. For each error, write:

---

## Entry 1

### 1. Error message
*copy it exactly*
Traceback (most recent call last):
  File "/Users/florawillbebetta/HCDE 310/hcde310/hw2/part2.py", line 9, in <module>
    print (art["title"],"-",art.get("artist","Unknown"),"(" + art.get("year","Unknown") + ")")
                                                        ~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~
TypeError: can only concatenate str (not "int") to str

### 2. What I thought it meant
I thought that means .get() can only be applied on string, and I will need to convert any integer to string to use.get().

### 3. What it actually meant
Since "(" is a string, and "year" is integer, the plus sign(+) can only connect string to string, instead of string to integer.

### 4. The fix
"(" + str(art.get("year","Unknown")) 

## Entry 2

### 1. Error message
*copy it exactly*
line 9
    print (art["title"],"-",art.get("artist","Unknown"),"(" + str(art.get("year","Unknown") +")")
          ^
SyntaxError: '(' was never closed

### 2. What I thought it meant
The '(' in print (art["title"] was not closed, since there is a ^ under the parenthesis.

### 3. What it actually meant
in the line of : str(art.get("year","Unknown"), the str( didn't get to close itself.

### 4. The fix
print (art["title"],"-",art.get("artist","Unknown"),"(" + str(art.get("year","Unknown"))+")")