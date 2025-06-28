import threading
from time import sleep
from . import commands_util
from datetime import datetime


def Uhr():
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    text = f"Die aktuelle Uhrzeit ist {current_time}"
    commands_util.say(text)


def Timer(stunden, stunde, minuten, minute, sekunden, sekunde):

    if stunden < 0:
        stunden += 1
    if stunde < 0:
        stunde += 1

    if minuten < 0:
        minuten += 1
    if minute < 0:
        minute += 1

    if sekunden < 0:
        sekunden += 1
    if sekunde < 0:
        sekunde += 1

    stunden = stunden+stunde
    minuten = minuten+minute
    sekunden = sekunden+sekunde
    print("Stunden: " + str(stunden))
    print("Minuten: " + str(minuten))
    print("Sekunden: " + str(sekunden))

    sekunden = stunden*3600+minuten*60+sekunden

    TimerThread = threading.Thread(target=setTimer, args=(sekunden,))
    commands_util.say("Timer gestartet")
    TimerThread.start()


def setTimer(sekunden):

    for i in range(sekunden):
        print(i)
        sleep(1)

    WIEDERHOLUNGTIMERENDE = 4
    for _ in range(WIEDERHOLUNGTIMERENDE):
        commands_util.say("Timer fertig")
        sleep(4)
