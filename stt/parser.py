from text_to_num import text2num

# Functionsweise
# Keyword suchen also z.B ["Uhr", "Uhrzeit"], wenn gefunden.
# Daten nehmen und extrahieren, wenn nichts extrahieren dann einfach function machen
GlobalInput = ""

callName = "hey alexa"


def SimpleCommand(Trigger, Input, Keywords):
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


def Command(Trigger, Input, Keywords, Infos):
    if not Keywords:
        print("Add Keywords!")
        return

    if not Infos:
        print("Benutzen Sie SimpleCommand, wenn Sie keine Infos benutzen wollen!")
        return

    for keyword in Keywords:
        if keyword not in Input:
            print(f"Keyword '{keyword}' nicht im Input.")
            return

    args = []
    words = Input.split()

    for _type, arg1, arg2 in Infos:
        if _type == "s":
            try:
                if arg2 == " ":
                    start = words.index(arg1) + 1
                    zwischen = words[start:len(words)]
                    args.append(" ".join(zwischen))
                else:
                    start = words.index(arg1) + 1
                    end = words.index(arg2)
                    zwischen = words[start:end]
                    args.append(" ".join(zwischen))
            except ValueError as e:
                args.append("__nothing__")
                # print(
                #    f"[Fehler - 's'] Wort '{arg1}' oder '{arg2}' nicht im Input gefunden.")
                # return

        elif _type == "n":
            try:
                index = words.index(arg1)
                if arg2 == "Left":
                    if index > 0:
                        leftNum = words[index - 1]
                        num = int(leftNum)
                        args.append(num)
                    else:
                        print(f"[Fehler - 'n'] Kein Wort links von '{arg1}'.")
                        return

                elif arg2 == "Right":
                    if index + 1 < len(words):
                        rightNum = words[index + 1]
                        num = int(rightNum)
                        args.append(num)
                    else:
                        print(f"[Fehler - 'n'] Kein Wort rechts von '{arg1}'.")
                        return
            except ValueError:
                args.append(-1)
                # print(f"[Fehler - 'n'] Wort '{arg1}' nicht im Input gefunden.")
                # return
            except Exception as e:
                print(f"[Fehler - 'n'] {e}")
                return
        else:
            print(f"Unbekannter Info-Typ: {_type}")
            return

    print("Argumente:", args)
    if len(args) == len(Infos):
        Trigger(*args)
    else:
        print("Fehler: Argumentanzahl stimmt nicht mit Infos überein.")


def Test1():
    print("jaaaj")


def Test2(todo):
    print("Das Todo ist " + todo)


def Test3(stunden, minuten, sekunden):
    print("Der timer ist: " + str(stunden) + "Stunde(N) " +
          str(minuten) + "Minute(n) " + str(sekunden) + "Sekunde(n)")
    pass


def convert_text2num(text):
    try:
        # Versuche den gesamten Text als Zahl zu interpretieren
        zahl = text2num(text, "de")
        return str(zahl)
    except Exception:
        # Falls nicht ganze Zahl, dann splitten und Wort für Wort wandeln
        wörter = text.split()
        neu = []
        for w in wörter:
            try:
                neu.append(str(text2num(w, "de")))
            except Exception:
                neu.append(w)
        return " ".join(neu)


def parse(input):
    print("Der Input ist: " + input)
    if callName in input:
        ergebnis = input.split(callName, 1)[1]

        ergebnis = convert_text2num(ergebnis)

        global GlobalInput
        GlobalInput = ergebnis
        print("Das ergebnis: " + ergebnis.strip())

        SimpleCommand(Test1, GlobalInput, ["uhr"])

        Command(Test2,  GlobalInput, [
            "todo"], [("s", "todo", "hinzu")])
        Command(Trigger=Test3, Input=GlobalInput, Keywords=[
                "timer"], Infos=[("n", "stunden", "Left"), ("n", "minuten", "Left"), ("n", "sekunden", "Left")])
