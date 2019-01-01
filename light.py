from gpiozero import LED
import time
led = LED(18)

led.on()
for i in range (5):
    print(i+1 , "s")
    time.sleep(1)

led.off()
