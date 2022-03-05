from server import Server
import client

import sys

argv = sys.argv

type = "client"
debug = False

for arg in argv:
	if arg == "--server":
		type = "server"
	if arg == "--debug":
		debug = True

if type == "server":
	server = Server()
	server.Run(3030)
else:
	cl = client.GameClient(debug)
	cl.OnRun()
