# class EquipmentStatus(enumerate):

class Equipment(object):
    def __init__(self, kind, ip, port):
        self.kind = kind
        self.ip = ip
        self.port = port

    def send_status(self):
        pass

    def run(self):
        pass


class Sensor(Equipment):
    def __init__(self, kind, ip, port):
        super(Sensor, self).__init__(kind, ip, port)
        self.value = None

    def set_value(self, new_value):
        self.value = new_value

    def send_value(self):
        pass


class Actuator(Equipment):
    def __init__(self, kind, ip, port):
        super(Sensor, self).__init__(kind, ip, port)
        self.status = None

    def set_status(self, new_status):
        self.status = new_status

    def receive_cmd(self, cmd):
        pass
