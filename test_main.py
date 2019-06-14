import pytest
from main import BoothInUseLedIndicator

### todo: is there a better way to mock?
# from pytest_mock import mocker 

from mock import Mock

try:
    import machine
    isRunningOffChip = False
except:
    from machine_stub import machine
    isRunningOffChip = True

@pytest.fixture
def boothInUseLedIndicator(monkeypatch, mockGreenLedPin, mockRedLedPin):
    monkeypatch.setattr("main.BoothInUseLedIndicator.greenLed", mockGreenLedPin) 
    monkeypatch.setattr("main.BoothInUseLedIndicator.redLed", mockRedLedPin) 
    return BoothInUseLedIndicator()
    
@pytest.fixture
def mockGreenLedPin():
    return Mock(spec=machine.Pin)

@pytest.fixture
def mockRedLedPin():
    return Mock(spec=machine.Pin)

class TestPinTransitions(object):

    def test_whenOccupiedThenTurnRedOnAndTurnGreenOff(self, monkeypatch, boothInUseLedIndicator, mockGreenLedPin, mockRedLedPin):
        boothInUseLedIndicator.setOccupied()
        mockGreenLedPin.off.assert_called()
        mockRedLedPin.on.assert_called()

    def test_whenAvailableThenTurnRedOffAndTurnGreenOn(self, monkeypatch, boothInUseLedIndicator, mockGreenLedPin, mockRedLedPin):
        boothInUseLedIndicator.setAvailable()
        mockGreenLedPin.on.assert_called()
        mockRedLedPin.off.assert_called()
