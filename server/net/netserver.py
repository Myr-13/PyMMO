from socket import socket
from uuid import uuid4, UUID

from logging.logging import Logger
from .netconnection import NetConnection

class NetServer:
	socket: socket
	connections: dict[UUID, NetConnection]

	logger: Logger

	def __init__(self, logger: Logger = Logger()) -> None:
		self.logger = logger

		self.socket = socket()
		self.connections = dict()

	def start(self, address: str = None, port: int = 3030) -> None:
		self.socket.bind((address or "", port))
		self.socket.listen(1)

		self.logger.log(f"Server started at {(address or 'localhost')}:{port}")

	def accept(self) -> None:
		connection, address = self.socket.accept()
		id = uuid4()

		self.connections[id] = NetConnection(connection, address, id, self, self.logger)