from text_to_num import text2num
import threading
import time
import pyttsx3

from stt.commands.commandsList import exec_commands


engine = pyttsx3.init()

GlobalInput = ""
callName = "hey alexa"


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

        exec_commands(GlobalInput)
