from ctypes import *

class CLedController():

    def __init__( self ):
        self.led = CDLL( "./ledCont.so" )

        self.led.WGsetup()

    def ledControl( self, pin, mode ):
        self.led.ledControl( pin, mode )