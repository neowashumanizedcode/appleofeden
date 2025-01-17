import time
import board
import neopixel
import touchio
import adafruit_dotstar

pixel_pin = board.D3
touch_pad = board.A0

num_pixels = 19

led = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1)
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.7, auto_write=False)

RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
OFF = (0, 0, 0)

touch = touchio.TouchIn(touch_pad)

class Effects:
    def __init__(self,ledStrip,colour,speed,tailLength, restartDelay): 
        self.ledStrip = ledStrip
        self.speed = speed
        self.timeRef = time.monotonic()
        self.xRef = 0
        self.numPixels = len(self.ledStrip)
        self.tail = tailLength
        self.OFF = (0, 0, 0)
        self.sequenceComplete = False
        self.restartDelay = restartDelay
        self.colour = colour
        self.effect = "commet"
        self.reverse = True
        self.fadeDuration = 5
        self.fadeSteps = self.fadeDuration * 2 * 10
        self.fadeUp = True
        self.rValue = self.colour[0]
        self.gValue = self.colour[1]
        self.bValue = self.colour[2]

    def reset(self):
        self.xRef = 0
        self.sequenceComplete = False
        self.fadeUp = True

    def animate(self):
        now = time.monotonic()
        
        #sequence for commet effect
        if self.effect == "commet":
            if self.xRef >= self.numPixels + self.tail+1 :
                self.sequenceComplete = True

            if now >= (self.timeRef + self.restartDelay) and self.sequenceComplete == True:
                self.reset()

            if self.sequenceComplete == False:
                if now >= self.timeRef + self.speed:
                    self.ledStrip.fill(OFF)
                    if self.xRef >=0 and self.xRef < self.numPixels:
                        #print(f"x is now {self.x}")
                        self.ledStrip[self.xRef] = self.colour
                    for y in range(1,self.tail+1):
                        if (self.xRef-y) >=0 and (self.xRef-y)<self.numPixels:
                            #print(f"y value is {self.x-y}")
                            colourFactor = 1/(10*y*y/2)
                            self.ledStrip[self.xRef-y]=(int(self.colour[0]*colourFactor),int(self.colour[1]*colourFactor),int(self.colour[2]*colourFactor))
                    self.ledStrip.show()
                    self.xRef+=1
                    self.timeRef = now

        elif self.effect == "fadeUpfadeDown":
            
            rstepValue = self.rValue/self.fadeSteps
            gstepValue = self.gValue/self.fadeSteps
            bstepValue = self.bValue/self.fadeSteps
            
            if self.fadeUp == True:
                
                if self.xRef == self.fadeSteps:
                    self.fadeUp = False
                    self.ledStrip.fill(self.colour)
                    self.ledStrip.show()
                
                elif now >= self.timeRef + 0.01:
                    self.ledStrip.fill((int(rstepValue*self.xRef),int(gstepValue*self.xRef),int(bstepValue*self.xRef)))
                    self.ledStrip.show()
                    self.xRef += 1
                    self.timeRef = now
                        
            elif self.fadeUp == False:
                
                if self.xRef == 0:
                    self.ledStrip.fill((0,0,0))
                    self.reset()
                
                elif now >= self.timeRef + 0.01:
                    self.ledStrip.fill((int(rstepValue*self.xRef),int(gstepValue*self.xRef),int(bstepValue*self.xRef)))
                    self.ledStrip.show()
                    self.xRef -= 1
                    self.timeRef = now
                    
        elif self.effect == "solidColour":
            self.ledStrip.fill(self.colour)
            self.ledStrip.show()
        #add reverse effect

pixelsEffects = Effects(pixels,YELLOW,0.05,4,3)

loopValue = 0

while True:
    if touch.value:
        led.fill(RED)
        led.show()
        loopValue += 1
        pixelsEffects.reset()
        print(f"loop value is {loopValue}")
        time.sleep(1)
        led.fill(OFF)
        led.show()

    if loopValue == 0:
        pixelsEffects.effect = "commet"
        pixelsEffects.colour = YELLOW
        pixelsEffects.animate()

    elif loopValue == 1:
        pixelsEffects.effect = "fadeUpfadeDown"
        pixelsEffects.colour = YELLOW
        pixelsEffects.animate()
                
    elif loopValue == 2:
        pixelsEffects.effect = "solidColour"
        pixelsEffects.colour = YELLOW
        pixelsEffects.animate()
    
    elif loopValue == 3:
        pixelsEffects.colour = OFF
        pixelsEffects.animate()
    
    else:
        pixelsEffects.reset()
        loopValue = 0
        
