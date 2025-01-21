This code was prepared to work on an Adafruit Trinket MO - read here to find out more on this micro-controller - https://learn.adafruit.com/adafruit-trinket-m0-circuitpython-arduino?view=all
This micro-controller can run both Arduino and Circuitpython and this code was done in python.
I used MU Editor to copy and modify this code to the controller - https://codewith.mu/en/download

Circuitpyathon Version - 8.2.7
https://circuitpython.org/board/trinket_m0/

Libraries required:
- neopixel
- adafruit_dotstar

Make sure to use the correct library set based on the version of python used:
https://circuitpython.org/libraries

In this example, pin A0 is used for cap touch.
There are three touch capable pins on the Trinket: A0, A3, and A4.

In this example, pin D3 is used for the pixel strip out.
You can also use PINs D0, D1, D2, D4 as well.

I use pin VBAT for Battery + (connected to Micro-Lipo Charger pin BAT)
and pin GND for ground (connected to one of the Micro-Lipo Charger GND pins)

The best part about this code is that I create a single class instance for the strip loading all the effects on the same class and use time.monotonic() to time the change in the effect sequences instead of time.sleep().
This way, you can run the effects on multiple PINs and can toggle between effects without having to wait until the end of and effects sequence.

You'll note I add time.sleep(1) if the touch PIN is touched to pause 1 second before cycling the effect, which also turns the trinket onboard dotstar on to RED to show it's been touched before turning it off.

Lastly, I increment a variable called "loopValue" to set the logic on what effect to run. 
When turned on - loop value == 0
the Effect is set to "commet
colour YELLOW
 and lastly, the method animate() cycles through the effect
