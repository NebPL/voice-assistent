import vosk
import sounddevice as sd
import sys
import queue
import json
from stt.parser import parse
import utils

q = queue.Queue()


def callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))


model = vosk.Model(
    "/Users/ben/home/programming/personal/voice-assisent/stt/vosk-model-small-de-0.15")


with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                       channels=1, callback=callback):
    rec = vosk.KaldiRecognizer(model, 16000)

    print("Du kannst jetzt sprechen...")

    while True:
        data = q.get()

        if rec.AcceptWaveform(data):
            result = rec.Result()
            text = json.loads(result).get("text", "")

            if text:
                print("Erkant: ", text)
                utils.util_logger.log("Erkannt: " + text)
                parse(text)

        else:
            partial_result = rec.PartialResult()
            partial_text = json.loads(partial_result).get("partial", "")
            if partial_text:
                print("Zwischenergebnis:", partial_text)
