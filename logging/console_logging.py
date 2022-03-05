import datetime
import colorama

from logging.logging import Logger

colorama.init(convert = True)

class ConsoleLogger(Logger):
	def __init__(self) -> None:
		super().__init__()

	def log(self, text: str):
		print(colorama.Fore.WHITE + "[{time}][LOG] - {text}".format(time = datetime.datetime.now().strftime("%H:%M:%S"), text=text))
	
	def warning(self, text: str):
		print(colorama.Fore.YELLOW + "[{time}][WARNING] - {text}".format(time = datetime.datetime.now().strftime("%H:%M:%S"), text=text))
	
	def error(self, text: str):
		print(colorama.Fore.RED + "[{time}][ERROR] - {text}".format(time = datetime.datetime.now().strftime("%H:%M:%S"), text=text))