from logging.logging import Logger
from protocol import PACKET_DELEMITER, NETPACK_TYPE_PLAYERCONNECT, NETPACK_TYPE_PLAYERDISCONNECT
from server.net.netconnection import NetConnection
from server.net.netserver import NetServer

class Parser:
	logger: Logger

	def __init__(self, logger: Logger = Logger()):
		self.logger = logger

	def parse(self, connection: NetConnection, string: str):
		data = string.split(PACKET_DELEMITER)

		if len(data) == 0:
			raise Exception("data is empty")
		
		action_type = int(data[0])

		{
			NETPACK_TYPE_PLAYERCONNECT: self.action_connect,
			NETPACK_TYPE_PLAYERDISCONNECT: self.action_disconnect
		}[action_type](connection)

	def action_connect(self, connection: NetConnection):
		self.logger.log(f"New connections from: {connection.address}")
		
	def action_disconnect(self, connection: NetConnection):
		connection.disconnect()