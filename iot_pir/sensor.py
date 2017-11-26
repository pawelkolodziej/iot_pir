import RPi.GPIO as GPIO
import time
import communication as com

GPIO.setmode(GPIO.BCM)
pir = 21
GPIO.setup(pir, GPIO.IN)
time.sleep(2)

def startDetectMotion():
    print "Detecting motion"
    while True:
        if GPIO.input(pir):
            com.printMotion()
            #com.saveToHtml()
            #com.sendNotoficationMotion()
            com.sendToThingsPeak()
            time.sleep(2)                               #D1- Delay to avoid multiple detection
        time.sleep(0.1)                                #While loop delay should be less than detection(hardware) delay