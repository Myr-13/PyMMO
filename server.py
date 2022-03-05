import socket
import threading as th

sock = socket.socket()

conns = []
addrs = []

def AcceptConnections():
	while True:
		conn, addr = sock.accept()

		print("New connections from: {}".format(addr))

		conns.append(conn)
		addrs.append(addr)

def RunServer(port):
	sock.bind(("", port))
	sock.listen(1)

	listener = th.Thread(target = AcceptConnections)
	listener.start()

	while True:
		for i in range(len(conns)):
			try:
				data = conns[i].recv(1024)

				if not data:
					continue

				print("Send to {addr} : {text}".format(addr = addrs[i], text = data.decode()))
				conns[i].send(data.upper())
			except:
				try:
					conns.pop(i)
					addrs.pop(i)
				except:
					pass

				print("User disconnected")
