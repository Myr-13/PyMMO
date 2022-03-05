import datetime

from .logging import Logger

class ConsoleLogger(Logger):
	def __init__(self) -> None:
		super().__init__()

	def log(self, text: str):
		print("[{time}][LOG] - {text}".format(time = datetime.time.now(), text=text))
	
	def warning(self, text: str):
		print("[{time}][WARNING] - {text}".format(time = datetime.time.now(), text=text))
	
	def error(self, text: str):
		print("[{time}][ERROR] - {text}".format(time = datetime.time.now(), text=text))