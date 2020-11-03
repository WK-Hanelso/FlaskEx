from ctypes import *


class LedController():

    def __init__( self ):
        self.led = CDLL( "./ledCont.so")

        self.dictColorPin = { 'r': 1, 'y': 4, 'g': 5 }

        self.led.WGsetup()

    def controlLed( self, color, mode ):

        dictColorPin = {}

        if mode not in [0,1]:
            print("error mode")

        if type( color ) != list:
            print( "error color")

        for tmpStr in color:
            if tmpStr in self.dictColorPin.keys():
                dictColorPin[ tmpStr ] = self.dictColorPin[ tmpStr ]

        for tmp in dictColorPin.keys():
            self.led.ledControl( self.dictColorPin[ tmp ], mode )

    def controlAllLed( self, mode ):

        for tmpStr in self.dictColorPin.keys():
            self.led.ledControl( self.dictColorPin[ tmpStr ], mode )

