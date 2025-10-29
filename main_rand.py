def parse_text(text):
    new_text = None
    limit = 15
    for x in range(len(text)//limit+1):
        offset = 0
        if x == 0:
            continue
        elif x == 1:
            while True:
                if text[x*limit-offset-1] == " ":
                    # text[x*10-offset] = "\n"
                    print("2nd itteration, whitespace: ", x*limit-offset)
                    new_text = text[:x*limit-offset-1] + "\n" + text[x*limit-offset:]
                    break
                elif offset >= limit:
                    # text[x * 10 - offset] = "\n"
                    new_text = text[:x*limit-offset-1] + "\n" + text[x*limit-offset:]
                    break
                else:
                    offset += 1
        else:
            while True:
                if text[x*limit-offset-1] == " ":
                    # text[x*10-offset] = "\n"
                    print("later itteration, whitespace: ", x*limit-offset)
                    new_text = new_text[:x*limit-offset] + "\n" + new_text[x*limit-offset:].strip()
                    break
                elif offset >= limit:
                    # text[x * 10 - offset] = "\n"
                    new_text = new_text[:x*limit-offset] + "\n" + new_text[x*limit-offset:].strip()
                    break
                else:
                    offset += 1
    return new_text
print(parse_text("1234567 1 123"))
# print(parse_text("lol and null").find("\n"))
def build_first():
    full_text: list[str] = []

def draw():
    for x in range(3):
        if x == 0:
            a = 1 #first column
        elif x == 1:
            a = 1 #2nd column
        elif x == 2:
            a = 1 #3rd column

