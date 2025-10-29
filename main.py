def parse_text(text: str):
    limit = 10
    past_ws_index = 0
    index = 0
    while True:
        if text.find(" ", index + 1) > 0:
            index = text.find(" ", index + 1)
            if index - past_ws_index > limit:
                text = text[:index] + "\n" + text[index+1:]
                past_ws_index = index
        else:
            break
    return text

def to_list(text: str):
    return text.split("\n")

# print(parse_text("one, two, three, four, five, six"))
# print(to_list(parse_text("one, two, three, four, five, six")))

def build_first():
    full_text: list[str] = []
    file = open("functions.txt", "r")
    for i, x in enumerate(file.readlines()):
        if x[1] != "n":
            full_text.append(x.split(":"))
    print(full_text)
    return full_text

list2 = []
list3 = [] # to be done later, parse and create the string lists for the other columns
def draw():
    for x in range(max(len(text), len(list2), len(list3))): # rows
        for y in range(3):
            if y == 0:
                for z in text[x][:3]:
                    print(z, end=" ")
                print()
                print(f"arg_1: {text[x][3]}, arg_2: {text[x][4]}, arg_3: {text[x][5]}")
                print(text[x][6])
                print()
            elif y == 1:
                a = 1 #2nd column
            elif y == 2:
                a = 1 #3rd column
            print()

text = build_first()
while True:
    draw()
    print()
    next_op = input("next op?")