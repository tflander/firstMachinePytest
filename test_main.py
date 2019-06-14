import pytest
from main import ClassUnderTest, ThingToMock
from pytest_mock import mocker 
from function import square, main

class TestClass(object):

    def test_real(self):
        sut = ClassUnderTest()
        assert  sut.doit() == "ThingToMock.doThing() called with stub for now"

    def test_mock(self, monkeypatch):
        monkeypatch.setattr("main.ThingToMock.doThing", lambda s,p: "mocked") 
        sut = ClassUnderTest()
        assert  sut.doit() == "mocked"

def test_mock(monkeypatch):
    monkeypatch.setattr("main.ThingToMock.doThing", lambda s,p: "mocked") 
    sut = ClassUnderTest()
    assert  sut.doit() == "mocked"

