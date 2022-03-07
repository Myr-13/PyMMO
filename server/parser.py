from logging.logging import Logger
from protocol import PACKET_DELEMITER, NETPACK_TYPE_PLAYERCONNECT, NETPACK_TYPE_PLAYERDISCONNECT

class Parser:
	def __init__(self, server, logger: Logger):
		self.server = server
		self.logger = logger

	def parse(self, string: str):
		data = string.split(PACKET_DELEMITER)

		if len(data) == 0:
			raise Exception("data is empty")
		
		action_type = int(data[0])
		