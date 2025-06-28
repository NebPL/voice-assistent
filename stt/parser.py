from text_to_num import text2num
import threading
import time
import pyttsx3

engine = pyttsx3.init()

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


def Trigertimer(stunden, minuten, sekunden):

    if stunden == -1:
        stunden = 0
    if minuten == -1:
        minuten = 0
    if sekunden == -1:
        sekunden = 0

    gesamtSekunden = stunden*3600 + minuten*60 + sekunden

    confirmSentance = "Timer gestellt für"

    if not stunden == -1:
        if stunden > 1:
            confirmSentance += str(stunden) + "stunden"
        else:
            confirmSentance += str(stunden) + "stunde"

    if not minuten == -1:
        if minuten > 1:
            confirmSentance += str(minuten) + "minuten"
        else:
            confirmSentance += str(minuten) + "minute"
    if not sekunden == -1:
        if sekunden > 1:
            confirmSentance += str(sekunden) + "sekunden"
        else:
            confirmSentance += str(sekunden) + "sekunden"

    engine.setProperty('rate', 175)
    engine.say(confirmSentance)
    engine.runAndWait()

    timerThread = threading.Thread(target=timer, args=(gesamtSekunden,))
    timerThread.start()


def timer(sekunden):
    sekundenTimer = sekunden

    for i in range(sekunden):
        time.sleep(1)
        print(i)

    engine.setProperty('rate', 175)
    engine.say("Timer ist zu ende")
    engine.runAndWait()


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


# Wörter, die ersetzt werden sollen
        ersetzen = {
            "eine": "1",
            "stunde": "stunden",
            "minute": "minuten",
            "minute": "minuten",
        }

# Durch Wörter gehen und ersetzen
        for alt, neu in ersetzen.items():
            ergebnis = ergebnis.replace(alt, neu)

        global GlobalInput
        GlobalInput = ergebnis
        print("Das ergebnis: " + ergebnis.strip())

        Command(Trigger=Trigertimer, Input=GlobalInput, Keywords=[
                "timer"], Infos=[("n", "stunden", "Left"), ("n", "minuten", "Left"), ("n", "sekunden", "Left")])
