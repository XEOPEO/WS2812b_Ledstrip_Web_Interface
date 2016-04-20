from socketIO_client import SocketIO, BaseNamespace
from neopixel import Adafruit_NeoPixel, Color
from enum import Enum, unique
import time

class LedStrip:
    def numLEDs(self):
        return self._obj.numPixels()

    @unique
    class Color(Enum):
        BLACK = Color(0, 0, 0)
        RED = Color(255, 0, 0)
        GREEN = Color(0, 0, 255)
        BLUE = Color(0, 255, 0)
        CYAN = Color(0, 255, 255)
        YELLOW = Color(255, 0, 255)
        PINK = Color(255, 255, 0)
        ORANGE = Color(255, 0, 127)

    def __init__(self, obj):
        self._obj = obj
        self.turnOff()

    def turnOff(self):
        for i in range(self.numLEDs()):
            self._obj.setPixelColor(i, Color.BLACK)
            self._obj.show()
            time.sleep(.1)

    def colorWipe(self, color, wait_sec=.05):
        ''' Wipe color across strip a pixel at a time '''

        for i in range(self.numLEDs()):
            self._obj.setPixelColor(i, color)
            self._obj.show()
            time.sleep(wait_sec)

    def theaterChase(self, color, wait_sec=.05, it=10):
        ''' Movie theater light style chaser animation '''

        for j in range(it):
            for q in range(3):
                for i in range(0, self.numLEDs(), 3):
                    self._obj.setPixelColor(i + q, color)
                
                self._obj.show()
                time.sleep(wait_sec)

                for i in range(0, self.numLEDs(), 3):
                    self._obj.setPixelColor(i + q, 0)

    def wheel(self, pos):
        ''' Generate rainbow colors across 0-255 positions '''

        if pos < 85: return Color(pos * 3, 255 - pos * 3, 0)
	elif pos < 170:
            pos -= 85
            return Color(255 - pos * 3, 0, pos * 3)
	else:
            pos -= 170
            return Color(0, pos * 3, 255 - pos * 3)

    # Functions depending on the "wheel" function
    # ---
    def rainbow(self, wait_sec=.02, it=1):
        ''' Draw rainbow that fades across all pixels at once '''

        for j in range(256 * it):
            for i in range(self.numLEDs()):
                self._obj.setPixelColor(i, self.wheel((i + j) & 255))

            self._obj.show()
            time.sleep(wait_sec)

    def rainbowCycle(self, wait_sec=.02, it=5):
        ''' Draw rainbow that uniformly distributes itself across all pixels '''

        for j in range(256 * it):
            for i in range(self.numLEDs()):
                self._obj.setPixelColor(i, self.wheel(((i * 256 / self.numLEDs()) + j) & 255))

            self._obj.show()
            time.sleep(wait_sec)

    def theaterChaseRainbow(self, wait_sec=.05):
        ''' Rainbow movie theater light style chaser animation '''

        for j in range(256):
            for q in range(3):
                for i in range(0, self.numLEDs(), 3):
                    self._obj.setPixelColor(i + q, self.wheel((i + j) % 255))

                self._obj.show()
                time.sleep(wait_sec)

                for i in range(0, self.numLEDs(), 3): self._obj.setPixelColor(i + q, 0)
    # ---

class DefaultNamespace(BaseNamespace):
    def on_connect(self):
        print '[Connected]'
        self.join('join', 'heyoo')

    def on_command(self, *args):
        data = str(args[0]['message'])
        # TODO: Parse JSON object from server

    def on_disconnect(self):
        print '[Disconnected]'
        socketIO.disconnect()

if __name__ == '__main__':
    socketIO = SocketIO('127.0.0.1', 5000, DefaultNamespace)
    socketIO.wait(for_connect=True, seconds=1)
