from . import commands_util


def Uhr():
    print("JAAA UHR GECALLED")


def exec_commands(input):
    commands_util.SimpleCommand(Trigger=Uhr, Input="test", Keywords=["test"])
