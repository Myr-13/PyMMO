from client.netclient import NetClient
import protocol

class InputData:
    def __init__(self):
        self.jump = 0
        self.move_dir = 0
        self.mouse_x = 1
        self.mouse_y = 0

class Controls:
    def __init__(self):
        self.input_data = InputData()

    def OnNetTick(self, net_client : NetClient):
        packet = protocol.NetPack_PlayerInput()
        packet.jump = self.input_data.jump
        packet.move_dir = self.input_data.move_dir
        packet.mouse_x = self.input_data.mouse_x
        packet.mouse_y = self.input_data.mouse_y

        net_client.Send(packet.Pack())
