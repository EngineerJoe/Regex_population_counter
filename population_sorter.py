# Allows regex
import re

# Sample text
text = (
    "Italy Roma 20 40 10 4902520 10290"
    "Italy Milan 20 10 49 20 1030"
    "Germany Berlin 20 10 10 10 29 490"
    "Germany Frankfurt 20 0 0 0 0"
    "Luxemburg Luxemburg 20 10 49"
)
# The regex search split into two sections
line_regex = re.compile(r"([A-Z]\w+\s[A-Z]\w+) ([0-9 ]+)")

# Empty dict to fill
loc_dict = {}

# Carries out code each time a match is found in the text
for match in re.finditer(line_regex, text):
    numbers = list(map(int, match.group(2).split(" ")))  # changes the big block of text into a list of ints
    total = sum(numbers)  # adds up all of the values in the numbers list
    loc_dict[match.group(1)] = {"numbers": numbers}  # makes a dict with numbers
    loc_dict[match.group(1)]['total'] = total  # makes a dict with the total

print(loc_dict)

# This is a simple code that allows the user to search for results in the dict

if __name__ == "__main__":
    while True:
        print(f"Choose location from list:\n{list(loc_dict.keys())}")
        message = input("Type here > ")
        if message in list(loc_dict.keys()):
            print(f"What data would you like: \n{list(loc_dict[message].keys())}")
            choice = input("Type here > ")
            if choice in loc_dict[message]:
                print(loc_dict[message][choice])
            else:
                print(f"{choice} not found")
        else:
            print(f"{message} not in list")
