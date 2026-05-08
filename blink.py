from gpiozero import LED
from time import sleep

led = LED(17)

while True:
    print("LED ON")
    led.on()
    sleep(1)

    print("LED OFF")
    led.off()
    sleep(1)
