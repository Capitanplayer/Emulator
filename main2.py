def parse_text(text):
    past_ws_index = 0
    limit = 10
    index = 0
    for x in text:
        if index % limit == 0:
            if text[index] == " ":
                text[index] == "\n"
                past_ws_index = index
            else:
                text[past_ws_index] = "\n"
        elif x == " ":
            text[index] = "\n"
        index += 1

print(parse_text("one, two, three, four, five, six"))
# print(parse_text("lol and null").find("\n"))
def build_first():
    full_text: list[str] = []
list1 = []
list2 = []
list3 = [] # to be done later, parse and create the string lists for the other columns
def draw():
    for x in range(max(len(list1), len(list2), len(list3))):
        for y in range(3):
            if y == 0:
                a = 1 #first column
            elif y == 1:
                a = 1 #2nd column
            elif y == 2:
                a = 1 #3rd column
