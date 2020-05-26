lstInput = []
def doFormating(phrase):
    interogative = ("how", "what", "why")
    capitalize = phrase.title()
    if phrase.startswith(interogative):
        return "{}?".format(capitalize)
    else:
        return "{}.".format(capitalize)


def doSentencePooling(phrase):
    sentence = doFormating(phrase)
    lstInput.append(sentence)


def doWork():
    while True:
        value = input("Say something: ")
        if value == "\\end":
            break
        else:
            doSentencePooling(value)

doWork()
print(" ".join(lstInput))
