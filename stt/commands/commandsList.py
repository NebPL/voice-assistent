from . import commands_util
from . import commands_triggers


def exec_commands(input):
    commands_util.SimpleCommand(
        Trigger=commands_triggers.Uhr, Input=input, Keywords=["uhr"])

    commands_util.command(
        Trigger=commands_triggers.Timer,
        Input=input,
        Keywords=["timer"],
        Infos=[("n", "stunden", "Left"),
               ("n", "stunde", "Left"),
               ("n", "minuten", "Left"),
               ("n", "minute", "Left"),
               ("n", "sekunden", "Left"),
               ("n", "sekunde", "Left"),
               ])
