import tkinter
import webbrowser


def get_oauth(url):
    webbrowser.open(url)


def get_config():
    f = open("etc/config.ini", "r", encoding="utf-8")
    configs = f.read().split("=")
    channel = configs[1].split('\n')[0]
    nick = configs[2].split('\n')[0]
    oauth = configs[3].split('\n')[0]
    f.close()
    return channel, nick, oauth


class Gui:

    channel_text = None
    nick_text = None
    oauth_text = None

    def __init__(self):
        self.root = tkinter.Tk()
        self.root.geometry("300x500+50+50")
        self.root.title("Configuration")
        self.game = False
        self.debug = False
        self.debugtk = tkinter.BooleanVar()

        configs = get_config()

        self.channel = tkinter.StringVar(self.root, configs[0])
        self.nick = tkinter.StringVar(self.root, configs[1])
        if configs[2] == "none":
            configs = (configs[0], configs[1], "")
        self.oauth = tkinter.StringVar(self.root, configs[2])

        self.btnconfig()
        self.textconfig()

    def mainloop(self):
        self.root.mainloop()

    def exit(self):
        self.game = True
        self.debug = self.debugtk.get()
        self.set_config()
        self.root.destroy()

    def btnconfig(self):
        url = "https://twitchapps.com""/tmi/"
        exit_button = tkinter.Button(self.root, text="Confirm", command=self.exit)
        exit_button.place(relx=0.5, rely=0.95, anchor="center")
        debug_button = tkinter.Checkbutton(self.root, text="Debug mode", variable=self.debugtk)
        debug_button.place(relx=0.5, rely=0.7, anchor="center")
        oauth = tkinter.Button(self.root, text="Get OAUTH token",
                               command=lambda aurl=url: get_oauth(aurl))
        oauth.place(relx=0.5, rely=0.47, anchor="center")

    def textconfig(self):
        label_config = tkinter.Label(self.root, text="Configuration")
        label_config.place(relx=0.5, rely=0.05, anchor="center")
        label_channel = tkinter.Label(self.root, text="Channel")
        label_channel.place(relx=0.5, rely=0.15, anchor="center")
        self.channel_text = tkinter.Entry(self.root, width=40, textvariable=self.channel, justify="center")
        self.channel_text.place(relx=0.5, rely=0.2, anchor="center")
        label_nick = tkinter.Label(self.root, text="Chat account")
        label_nick.place(relx=0.5, rely=0.25, anchor="center")
        self.nick_text = tkinter.Entry(self.root, width=40, textvariable=self.nick, justify="center")
        self.nick_text.place(relx=0.5, rely=0.3, anchor="center")
        label_oauth = tkinter.Label(self.root, text="OAUTH token")
        label_oauth.place(relx=0.5, rely=0.35, anchor="center")
        self.oauth_text = tkinter.Entry(self.root, width=40, textvariable=self.oauth, justify="center")
        self.oauth_text.place(relx=0.5, rely=0.4, anchor="center")

    def set_config(self):
        f = open("etc/config.ini", "w", encoding="utf-8")
        config = f"channel={self.channel_text.get()}" + '\n' + f"nickname={self.nick_text.get()}" + '\n'\
                 + f"oauth_token={self.oauth_text.get()}"
        f.write(config)
