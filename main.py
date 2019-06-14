try:
    import machine
except:
    from machine_stub import machine

greenLed = machine.Pin(22, machine.Pin.OUT)
redLed = machine.Pin(21, machine.Pin.OUT)

class BoothInUseLedIndicator:
    inUse = False

    def isInuse(self):
        return self.inUse

    def setOccupied(self, isInUse = True):
        self.inuse = isInUse
        if(self.inuse):
            greenLed.off()
            redLed.on()
        else:
            redLed.off()
            greenLed.on()
    
    def setAvailable(self):
        self.setOccupied(False)

class ThingToMock:
    def doThing(self, param):
        return "ThingToMock.doThing() called with " + param

class ClassUnderTest:

    thingx = ThingToMock()

    def doit(self):
        return self.thingx.doThing("stub for now")
