import logging
import socket
import time

from emoji import demojize


class Chat:
    def __init__(self):
        self.sock = socket.socket()

        server = 'irc.chat.twitch.tv'
        port = 6667

        f = open("etc/config.ini", "r", encoding="utf-8")
        configs = f.read().split("=")
        channel = "#" + configs[1].split('\n')[0]
        nickname = configs[2].split('\n')[0]
        token = configs[3].split('\n')[0]
        f.close()

        self.sock.connect((server, port))

        self.sock.send(f"PASS {token}\n".encode('utf-8'))
        self.sock.send(f"NICK {nickname}\n".encode('utf-8'))
        self.sock.send(f"JOIN {channel}\n".encode('utf-8'))

        f = open("etc/chat.log", "w", encoding="utf-8")
        f.write("")
        f.close()

        self.t = 0
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s — %(message)s',
                            datefmt='%Y-%m-%d_%H:%M:%S',
                            handlers=[logging.FileHandler('etc/chat.log', encoding='utf-8')])

    def log(self):
        while True:
            try:
                resp = self.sock.recv(2048).decode('utf-8')

                if resp.startswith('PING'):
                    self.sock.send("PONG\n".encode('utf-8'))

                elif len(resp) > 0:
                    logging.info(demojize(resp))

                self.t += 1
                if self.t == 3000:
                    f = open("etc/chat.log", "w", encoding="utf-8")
                    f.write("")
                    f.close()
            except:
                time.sleep(1)
