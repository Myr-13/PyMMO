from socket import socket
from typing_extensions import Self, TYPE_CHECKING
from uuid import UUID
from logging.logging import Logger

import protocol

if TYPE_CHECKING:
	from .netserver import NetServer

class NetConnection:
	connection: socket
	address: str
	id: UUID

	server: 'NetServer'
	logger: 'Logger'

	def __init__(self, connection: socket, address: str, id: UUID, server: 'NetServer', logger: 'Logger' = Logger()):
		self.connection = connection
		self.address = address
		self.id = id

		self.server = server
		self.logger = logger

	def disconnect(self) -> None:
		self.server.connections.pop(self.id)
		try:
			self.send(protocol.NetPack_PlayerDisconnect().Pack())
			self.close()
		except:
			pass

		self.logger.log(f"User '{self.address}' disconnected")

	def recive(self, buffer_size: int = 1024) -> bytearray:
		return self.connection.recv(buffer_size)

	def recive_all(self, pack_end: bytearray, buffer_size: int = 1024):
		data = bytearray()

		while True:
			chunk = self.recive(buffer_size)
			if not chunk:
				break
			data += chunk

			if data[-len(pack_end):] == pack_end:
				break
		
		return data

	def send(self, data: bytearray) -> Self:
		self.connection.send(data)
		return self
