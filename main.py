from server.server import Server
import client

import sys

argv = sys.argv

type = "client"
debug = False
console = False

for arg in argv:
	if arg == "--server":
		type = "server"
	if arg == "--debug":
		debug = True
	if arg == "--console":
		console = True

if type == "server":
	sv = Server()
	sv.run(3030)
else:
	cl = client.GameClient(debug, not console)
	cl.Run()
