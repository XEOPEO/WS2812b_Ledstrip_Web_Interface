from socketIO_client import SocketIO, BaseNamespace
from neopixel import Adafruit_NeoPixel, Color
import time
import json

class LedStrip:
    def numLEDs(self):
        return self._obj.numPixels()

    def setNeoPixel(self, obj):
        self._obj = obj
        self._obj.begin()
        self.turnOff()

    def getNeoPixel(self):
        return self._obj

    def setColorPixel(self, index, color, wait_sec=.05):
        self._obj.setPixelColor(index, color)
        self._obj.show()
        time.sleep(wait_sec)

    def __init__(self, obj=None):
        self._obj = obj

    def turnOff(self):
        for i in range(self.numLEDs()):
            self._obj.setPixelColor(i, Color(0, 0, 0))
            self._obj.show()
            time.sleep(.1)

    def colorWipe(self, color=Color(255, 0, 0), wait_sec=.05):
        ''' Wipe color across strip a pixel at a time '''

        for i in range(self.numLEDs()):
            self._obj.setPixelColor(i, color)
            self._obj.show()
            time.sleep(wait_sec)

    def theaterChase(self, color=Color(0, 255, 0), wait_sec=.05, it=10):
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

class StripNamespace(BaseNamespace):
    def on_connect(self):
        print '[Connected]'

    def on_command(self, *args):
        data = args[0]

        if 'index' in data and 'r' in data and 'g' in data and 'b' in data:
            data = json.loads(data)

            if isinstance(data['index'], int) and isinstance(data['r'], int) and isinstance(data['g'], int) and isinstance(data['b'], int):
                strip.setColorPixel(data['index'], Color(data['g'], data['r'], data['b']))

        if 'count' in data and 'brightness' in data:
            data = json.loads(data)

            if isinstance(data['count'], int) and isinstance(data['brightness'], int):
                strip.setNeoPixel(Adafruit_NeoPixel(data['count'], 18, 800000, 5, 0, data['brightness']))

        if strip.getNeoPixel is not None and 'index' not in data:
            data = str(data)

            if data == 'turnOff': strip.turnOff()
            elif data == 'colorWipe': strip.colorWipe()
            elif data == 'theaterChase': strip.theaterChase()
            elif data == 'rainbow': strip.rainbow()
            elif data == 'rainbowCycle': strip.rainbowCycle()
            elif data == 'theaterChaseRainbow': strip.theaterChaseRainbow()

    def on_disconnect(self):
        print '[Disconnected]'
        socketIO.disconnect()

if __name__ == '__main__':
    strip = LedStrip()
    socketIO = SocketIO('127.0.0.1', 8080)
    strip_namespace = socketIO.define(StripNamespace, '/strip')
    socketIO.wait(for_connect=True, seconds=1)
