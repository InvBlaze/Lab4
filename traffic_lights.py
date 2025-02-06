from gpiozero import LED

class TrafficLights:
    def __init__(self, red_pin, yellow_pin, green_pin):
        self.red = LED(red_pin)
        self.yellow = LED(yellow_pin)
        self.green = LED(green_pin)

    def red_light(self):
        """Turns on the Red light and turns off others"""
        self.red.on()
        self.yellow.off()
        self.green.off()

    def yellow_light(self):
        """Turns on the Yellow light and turns off others"""
        self.red.off()
        self.yellow.on()
        self.green.off()

    def green_light(self):
        """Turns on the Green light and turns off others"""
        self.red.off()
        self.yellow.off()
        self.green.on()
