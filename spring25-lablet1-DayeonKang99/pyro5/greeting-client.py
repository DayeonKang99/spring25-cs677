# saved as greeting-client.py
import Pyro5.api

name = input("What is your name? ").strip()
IP='172.17.0.2'
greeting_maker = Pyro5.api.Proxy(f"PYRONAME:example.greeting@{IP}")    # use name server object lookup uri shortcut
print(greeting_maker.get_fortune(name))
