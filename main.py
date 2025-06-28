from threading import Thread
import utils
import stt


def Stt():
    stt.start  # stt = speack to text


if __name__ == "__main__":
    thread_stt = Thread(target=Stt)
    thread_stt.start()
    thread_stt.join()
