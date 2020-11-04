from clibwrapper import CLedController


class LedController():

    dictColor = {}

    def __init__( self, listColor = [], nMode = 0 ):

        if type( listColor) != list:
            print("error color")

        if nMode not in [ 0, 1 ]:
            print("error mode")

        self.listColor = listColor
        self.nMode = nMode
        
        self.setDictColor( listColor )

        self.C_LED = CLedController()

    def setMode( self, nMode ):
        if nMode not in [ 0, 1 ]:
            print("not 0 or 1")
        else:
            self.nMode = nMode

    def setListColor( self, listColor ):
        if type( listColor ) != list:
            print( "not list")
        else:
            self.setDictColor( listColor )


    def setDictColor( self, listColor ):
        if 'r' in listColor:
            self.dictColor["RED"] = 1
        if 'y' in listColor:
            self.dictColor["YELLOW"] = 4
        if 'g' in listColor:
            self.dictColor["GREEN"] = 5

    def actLed( self ):

        for strKey in self.dictColor.keys():
            self.C_LED.ledControl( self.dictColor[ strKey ], self.nMode )

    def isSetColor( self, strKey ):
        return strKey in self.dictColor.keys()


