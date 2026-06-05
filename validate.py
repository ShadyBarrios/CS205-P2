# will include regex script to make sure file input is correct format
# (int) (x.xxxxxxxe+xx) (x.xxxxxxxe+xx) ...
import re as regex

# note: r needed for regex (raw string format)
pattern1 = r"[1-9]\.(0{7})e\+(0{2})" # int for class classification
pattern2 = r"\-?\d\.\d{7}e[\+\-]\d{2}" # (x.xxxxxxxe+xx)

def validate(lines):
    for line in lines:
        status = validateLine(line)
        if status == False:
            return False
    return True

def validateLine(line):
    items = line.split() # split at whitespace
    classItem = items[0]
    valueItems = items[1::]

    checkClass = regex.fullmatch(pattern1, classItem)
    if checkClass is None:
        return False
    
    for item in valueItems: # makes sure that each item matches the 8-floating num standard
        checkValue = not (regex.fullmatch(pattern2, item) is None)
        if checkValue == False:
            return False
    
    return True