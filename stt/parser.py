
# Functionsweise

# Keyword suchen also z.B ["Uhr", "Uhrzeit"], wenn gefunden.
# Daten nehmen und extrahieren, wenn nichts extrahieren dann einfach function machen
Input = ""

callName = "hey alexa"

def parse(input):

    if callName in input:
        ergebnis = input.split(callName, 1)[1]

        global Input
        Input = ergebnis
        print(ergebnis)
        


def SimpleCommand(Trigger, Keywords=[]):
    if not Keywords:
        print("Add Keywords!")
        pass

    for keyword in Keywords:
        if keyword in Input:
            if keyword == Keywords[-1]:
                Trigger()
        else:
            print("Keyword " + keyword + " ist nicht im Input!")
            break


def Command(Trigger, Keywords=[], Infos=[]):
    if not Keywords:
        print("Add Keywords!")
        pass

    if not Infos:
        print("Benutzen sie SimpleCommand wenn sie keine Infos benutzen wollen!")
        pass

    for keyword in Keywords:
        if not keyword in Input:
            pass

    args = []

    for _type, arg1, arg2 in Infos:

        words = Input.split()
        print(words)

        if _type == "s":

            if arg2 == " ":
                print("test")
                start = words.index(arg1) + 1
                zwischen = words[start:len(words)]
                args.append(zwischen)

            else:
                start = words.index(arg1) + 1
                end = words.index(arg2)
                zwischen = words[start:end]
                args.append(zwischen)

        if _type == "n":
            if arg2 == "Left":
                print("test1")
                print(Input)
                if arg1 in words:
                    print("test2")
                    index = words.index(arg1)

                    if index > 0:
                        leftNum = words[index-1]
                        num = int(leftNum)
                        print(num)
                        args.append(num)

            if arg2 == "Right":
                if arg1 in words:
                    index = words.index(arg1)

                    if index > 0:
                        leftNum = words[index+1]
                        num = int(leftNum)
                        print(num)
                        args.append(num)
            else:
                pass

    Trigger(*args)


def Test1(input1, input2, input3):
    print("Der Inputs waren: " + str(input1) + str(input2) + str(input3))


Command(Test1,  ["timer"], [("n", "Stunden", "Left"),
        ("n", "Minuten", "Left"), ("n", "Sekunden", "Left")])


def Test2(todo, bis):
    print("Todo" + str(todo))
    print("Bis" + str(bis))


Command(Test2,  [
        "todo"], [("s", "todo", "bis"), ("s", "bis", " ")])
