try:
    import machine
    isRunningOffChip = False
except:
    from machine_stub import machine
    isRunningOffChip = True

class BoothInUseLedIndicator:
    inUse = False
    greenLed = machine.Pin(22, machine.Pin.OUT)
    redLed = machine.Pin(21, machine.Pin.OUT)

    def isInuse(self):
        return self.inUse

    def setOccupied(self, isInUse = True):
        self.inuse = isInUse
        if(self.inuse):
            self.greenLed.off()
            self.redLed.on()
        else:
            self.redLed.off()
            self.greenLed.on()
    
    def setAvailable(self):
        self.setOccupied(False)
