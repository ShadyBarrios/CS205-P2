# will include regex script to make sure file input is correct format
# (int) (x.xxxxxxxe+xxx) (x.xxxxxxxe+xxx) ...
import re as regex

# note: r needed for regex (raw string format)
pattern1 = r"[1-9](\d*)" # int for class classification
pattern2 = r"[1-9]\.(\d{7})e\+(\d{3})" # (x.xxxxxxxe+xxx)

def validate(lines):
    for line in lines:
        status = validateLine(line)
        if status == False:
            return False
    return True

def validateLine(line):
    items = line.split(r"\w") # split at whitespace
    classItem = items[0]
    valueItems = items[1::]

    checkClass = regex.match(pattern1, classItem)
    if checkClass is None:
        return False
    
    for item in valueItems: # makes sure that each item matches the 8-floating num standard
        checkValue = not (regex.match(pattern2, item) is None)
        if checkValue == False:
            return False
    
    return True