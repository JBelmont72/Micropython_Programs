from machine import Pin, ADC, PWM
import network, socket
from time import sleep

class KitronikButton:
    def __init__(self, pin):
        self.button = Pin(pin, Pin.IN, Pin.PULL_DOWN)

    def pressed(self):
        return self.button.value()

class KitronikBuzzer:
    def __init__(self, pin):
        self.buzzer = PWM(Pin(pin))
        self.buzzer.freq(1000)

    def play(self):
        self.buzzer.duty_u16(30000)

    def stopTone(self):
        self.buzzer.duty_u16(0)

class MiniControllerUDPClient:
    def __init__(self, server_ip="192.168.1.50", port=5005):
        self.up = KitronikButton(18)
        self.down = KitronikButton(20)
        self.left = KitronikButton(19)
        self.right = KitronikButton(22)
        self.a = ADC(26)  # GP26 = ADC0
        self.b = ADC(27)  # GP27 = ADC1
        self.buzzer = KitronikBuzzer(5)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.addr = (server_ip, port)
        self.wlan = network.WLAN(network.STA_IF)
        self.wlan.active(True)
        self.wlan.connect("SpectrumSetup-41", "leastdinner914")
        while not self.wlan.isconnected():
            sleep(0.5)

    def send(self, msg):
        self.sock.sendto(msg.encode(), self.addr)

    def read_controls(self):
        if self.up.pressed():
            self.send("forward")
        elif self.down.pressed():
            self.send("backward")
        elif self.left.pressed():
            self.send("left")
        elif self.right.pressed():
            self.send("right")
        elif self.a.read_u16() > 50000:
            self.send("speedup")
        elif self.b.read_u16() > 50000:
            self.send("slowdown")
        else:
            self.send("stop")

if __name__ == "__main__":
    controller = MiniControllerUDPClient()
    print("Controller ready!")
    while True:
        controller.read_controls()
        sleep(0.1)
