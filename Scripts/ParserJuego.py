def parse():
    chat_log = open('etc/chat.log', "r", encoding="utf-8")
    chat = chat_log.read().split("\n\n\n")
    chat_parsed = open("etc/chat.txt", "w", encoding="utf-8")
    config = get_config()
    channel = config[0]
    nickname = config[1]
    lines = []
    try:
        for i in chat:
            if len(i) > 0:
                if "GLHF!" not in i:
                    if "PING" not in i:
                        if nickname != i.split(":")[2] and nickname != i.split(":")[4] \
                                and f"{nickname} = #{channel}" not in i.split("—")[1].split(":")[2]:
                            if len(i) > 0:
                                user = f"{i.split('—')[1].split(':')[1].split('!')[0]}"
                                msg = f"{i.split('—')[1].split(':')[2]}"
                                line = str(user + " — " + msg)
                                if not line.startswith("yastarth"):
                                    lines.append(line)

        for i in lines:
            chat_parsed.write(str(i))
            chat_parsed.write('\n')
        chat_log.close()
        chat_parsed.close()
    except IndexError:
        pass


def comprobar_chat():
    chat = open("etc/chat.txt", "r", encoding="utf-8")
    lineas = chat.readlines()
    lineas_prev = len(lineas)
    parse()
    chat.seek(0)
    lineas = chat.readlines()
    lineas_act = len(lineas)

    if lineas_act > lineas_prev:
        if len(lineas[lineas_act - 1].split(" — ")[0].split("'")) > 0:
            usr = lineas[lineas_act - 1].split(" — ")[0]
            return usr
    else:
        return None


def get_config():
    f = open("etc/config.ini", "r", encoding="utf-8")
    configs = f.read().split("=")
    channel = configs[1].split('\n')[0]
    nick = configs[2].split('\n')[0]
    f.close()
    return channel, nick
