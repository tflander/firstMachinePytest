# firstMachinePytest

I'm learning MicroPython for IoT, and would like to test-drive code (TDD).  I could not find any examples on test-driving MicroPython.
I found lots of examples of test-driving Python, and examples of writing MicroPython without tests, but not both at the same time.

While there may be benefits to running tests on-chip, I wanted to be able to run tests from my IDE.  For now I'm using Visual Studio Code.

The first problem was that I don't have a machine module to import on my mac.  The machine module is specific to the ESP32
ecosystem.  You get it when you burn the ESP32 chip with the MicroPython firmware, so it's only available on-chip.

I solved this problem by creating a stub machine module (machine_stub.py).  This has stubs for the machine features that I wanted to be able to mock.
There may be a better way.

The second problem is that I was unfamiliar with mocking in python. I found a YouTube video that demistified mocking: https://www.youtube.com/watch?v=RcN26hznmk4.
You can also search for "Improve your testing with Pytest and Mock - PyCon SG 2015"
