class Connector:
    def connect(self, other):
        pass


class ConnectHdmiCable(Connector):
    pass


class ConnectRcaCable(Connector):
    pass


class ConnectEthernetCable(Connector):
    pass


class ConnectPowerCable(Connector):
    pass


class Television:
    def __init__(self):
        self.connect_to_device_via_rca_cable = ConnectRcaCable()
        self.connect_to_device_via_hdmi_cable = ConnectHdmiCable()
        self.connect_device_to_power_outlet = ConnectPowerCable()


class DVDPlayer:
    def __init__(self):
        self.connect_to_device_via_hdmi_cable = ConnectHdmiCable()
        self.connect_device_to_power_outlet = ConnectPowerCable()


class GameConsole:
    def __init__(self):
        self.connect_to_device_via_hdmi_cable = ConnectHdmiCable()
        self.connect_to_device_via_ethernet_cable = ConnectEthernetCable()
        self.connect_device_to_power_outlet = ConnectPowerCable()


class Router:
    def __init__(self):
        self.connect_to_device_via_ethernet_cable = ConnectEthernetCable()
        self.connect_device_to_power_outlet = ConnectPowerCable()


tv = Television()
game_console = GameConsole()
tv.connect_to_device_via_hdmi_cable.connect(game_console)

# EXAMPLE TO FIX
# class EntertainmentDevice:
#     def connect_to_device_via_hdmi_cable(self, device): pass
#     def connect_to_device_via_rca_cable(self, device): pass
#     def connect_to_device_via_ethernet_cable(self, device): pass
#     def connect_device_to_power_outlet(self, device): pass
#
#
# class Television(EntertainmentDevice):
#     def connect_to_dvd(self, dvd_player):
#         self.connect_to_device_via_rca_cable(dvd_player)
#
#     def connect_to_game_console(self, game_console):
#         self.connect_to_device_via_hdmi_cable(game_console)
#
#     def plug_in_power(self):
#         self.connect_device_to_power_outlet(self)
#
#
# class dvd_player(EntertainmentDevice):
#     def connect_to_tv(self, television):
#         self.connect_to_device_via_hdmi_cable(television)
#
#     def plug_in_power(self):
#         self.connect_device_to_power_outlet(self)
#
#
# class GameConsole(EntertainmentDevice):
#     def connect_to_tv(self, television):
#         self.connect_to_device_via_hdmi_cable(television)
#
#     def connect_to_router(self, router):
#         self.connect_to_device_via_ethernet_cable(router)
#
#     def plug_in_power(self):
#         self.connect_device_to_power_outlet(self)
#
#
# class Router(EntertainmentDevice):
#     def connect_to_tv(self, television):
#         self.connect_to_device_via_ethernet_cable(television)
#
#     def connect_to_game_console(self, game_console):
#         self.connect_to_device_via_ethernet_cable(game_console)
#
#     def plug_in_power(self):
#         self.connect_device_to_power_outlet(self)