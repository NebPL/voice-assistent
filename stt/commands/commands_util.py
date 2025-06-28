from text_to_num import text2num


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
